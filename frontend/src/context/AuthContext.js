import React, { createContext, useState, useEffect } from 'react';
import axios from 'axios';

// Create context
const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Check if user is logged in on initial load
  useEffect(() => {
    const checkLoggedIn = async () => {
      // Check if token exists in local storage
      const token = localStorage.getItem('token');
      
      if (token) {
        // Set auth token header
        setAuthToken(token);
        
        try {
          // Verify token by getting user data
          const res = await axios.get('/users/profile/');
          setUser(res.data);
          setIsAuthenticated(true);
        } catch (err) {
          // Token is invalid
          localStorage.removeItem('token');
          setAuthToken(null);
          setUser(null);
          setIsAuthenticated(false);
          setError('Session expired. Please log in again.');
        }
      }
      
      setLoading(false);
    };
    
    checkLoggedIn();
  }, []);

  // Set auth token for axios
  const setAuthToken = (token) => {
    if (token) {
      axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
    } else {
      delete axios.defaults.headers.common['Authorization'];
    }
  };

  // Register user
  const register = async (userData) => {
    try {
      console.log('Tentative d\'inscription avec:', userData);
      const res = await axios.post('/users/register/', {
        username: userData.username,
        email: userData.email,
        password: userData.password,
        password2: userData.password2,
        bio: userData.bio || ''
      });
      console.log('Réponse d\'inscription:', res.data);
      return res.data;
    } catch (err) {
      console.error('Erreur d\'inscription:', err.response?.data || err.message);
      
      // Gérer les erreurs de validation
      if (err.response?.data) {
        const errorData = err.response.data;
        let errorMessage = '';
        
        // Convertir les erreurs de validation en message lisible
        Object.keys(errorData).forEach(key => {
          errorMessage += `${key}: ${errorData[key].join(', ')}\n`;
        });
        
        setError(errorMessage || 'L\'inscription a échoué');
      } else {
        setError('L\'inscription a échoué. Veuillez réessayer.');
      }
      
      throw err;
    }
  };

  // Login user
  const login = async (userData) => {
    try {
      console.log('Tentative de connexion avec:', userData);
      const res = await axios.post('/token/', {
        email: userData.email,
        password: userData.password
      });
      
      console.log('Réponse de connexion:', res.data);
      
      // Save token to local storage
      localStorage.setItem('token', res.data.access);
      
      // Set auth token in headers
      setAuthToken(res.data.access);
      
      // Get user data
      const userRes = await axios.get('/users/profile/');
      console.log('Données utilisateur:', userRes.data);
      setUser(userRes.data);
      setIsAuthenticated(true);
      setError(null);
      
      return res.data;
    } catch (err) {
      console.error('Erreur de connexion:', err.response?.data || err.message);
      setError(err.response?.data?.detail || 'Échec de connexion. Vérifiez vos identifiants.');
      throw err;
    }
  };

  // Logout user
  const logout = () => {
    // Remove token from local storage
    localStorage.removeItem('token');
    
    // Remove auth token from headers
    setAuthToken(null);
    
    // Reset state
    setUser(null);
    setIsAuthenticated(false);
  };

  // Update user profile
  const updateProfile = async (userData) => {
    try {
      const res = await axios.put('/users/me/', userData);
      setUser(res.data);
      return res.data;
    } catch (err) {
      setError(err.response?.data?.detail || 'Profile update failed');
      throw err;
    }
  };

  // Clear errors
  const clearError = () => {
    setError(null);
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        isAuthenticated,
        loading,
        error,
        register,
        login,
        logout,
        updateProfile,
        clearError
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

// Export context for use in components
AuthContext.displayName = 'AuthContext';
AuthProvider.context = AuthContext;
export default AuthContext;
