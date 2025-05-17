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
      // Afficher l'URL complète pour le débogage
      const registerUrl = `${axios.defaults.baseURL}/users/register/`;
      console.log('URL d\'inscription:', registerUrl);
      console.log('Tentative d\'inscription avec:', userData);
      
      // Ajouter des en-têtes supplémentaires pour le débogage
      const config = {
        headers: {
          'Content-Type': 'application/json',
          'X-Debug-Info': 'frontend-registration'
        },
        withCredentials: true
      };
      
      // Faire la requête avec les en-têtes personnalisés
      const res = await axios.post('/users/register/', {
        username: userData.username,
        email: userData.email,
        password: userData.password,
        password2: userData.password2,
        bio: userData.bio || ''
      }, config);
      
      console.log('Réponse d\'inscription:', res.data);
      alert('Inscription réussie! Vous pouvez maintenant vous connecter.');
      return res.data;
    } catch (err) {
      // Afficher des informations détaillées sur l'erreur
      console.error('Erreur d\'inscription complète:', err);
      console.error('Détails de la réponse:', err.response);
      console.error('Données d\'erreur:', err.response?.data);
      console.error('Statut HTTP:', err.response?.status);
      console.error('En-têtes:', err.response?.headers);
      
      // Gérer les erreurs de validation
      if (err.response?.data) {
        const errorData = err.response.data;
        let errorMessage = 'Erreurs d\'inscription:\n';
        
        // Convertir les erreurs de validation en message lisible
        if (typeof errorData === 'object') {
          Object.keys(errorData).forEach(key => {
            const value = errorData[key];
            if (Array.isArray(value)) {
              errorMessage += `${key}: ${value.join(', ')}\n`;
            } else {
              errorMessage += `${key}: ${value}\n`;
            }
          });
        } else if (typeof errorData === 'string') {
          errorMessage = errorData;
        }
        
        setError(errorMessage);
        alert(errorMessage); // Afficher l'erreur dans une alerte pour débogage
      } else {
        const errorMsg = `L'inscription a échoué: ${err.message || 'Erreur inconnue'}`;
        setError(errorMsg);
        alert(errorMsg); // Afficher l'erreur dans une alerte pour débogage
      }
      
      throw err;
    }
  };

  // Login user
  const login = async (userData) => {
    try {
      // Afficher l'URL complète pour le débogage
      const loginUrl = `${axios.defaults.baseURL}/token/`;
      console.log('URL de connexion:', loginUrl);
      console.log('Tentative de connexion avec:', userData);
      
      // Ajouter des en-têtes supplémentaires pour le débogage
      const config = {
        headers: {
          'Content-Type': 'application/json',
          'X-Debug-Info': 'frontend-login'
        },
        withCredentials: true
      };
      
      // Faire la requête avec les en-têtes personnalisés
      const res = await axios.post('/token/', {
        email: userData.email,
        password: userData.password
      }, config);
      
      console.log('Réponse de connexion:', res.data);
      
      // Save token to local storage
      localStorage.setItem('token', res.data.access);
      
      // Set auth token in headers
      setAuthToken(res.data.access);
      
      // Get user data
      const userRes = await axios.get('/users/profile/', {
        headers: {
          'Authorization': `Bearer ${res.data.access}`,
          'X-Debug-Info': 'frontend-profile'
        },
        withCredentials: true
      });
      
      console.log('Données utilisateur:', userRes.data);
      setUser(userRes.data);
      setIsAuthenticated(true);
      setError(null);
      
      return res.data;
    } catch (err) {
      // Afficher des informations détaillées sur l'erreur
      console.error('Erreur de connexion complète:', err);
      console.error('Détails de la réponse:', err.response);
      console.error('Données d\'erreur:', err.response?.data);
      console.error('Statut HTTP:', err.response?.status);
      console.error('En-têtes:', err.response?.headers);
      
      // Construire un message d'erreur détaillé
      let errorMessage = 'Échec de connexion: ';
      
      if (err.response?.data) {
        if (typeof err.response.data === 'object') {
          if (err.response.data.detail) {
            errorMessage += err.response.data.detail;
          } else {
            // Parcourir toutes les erreurs
            Object.keys(err.response.data).forEach(key => {
              const value = err.response.data[key];
              if (Array.isArray(value)) {
                errorMessage += `${key}: ${value.join(', ')}. `;
              } else {
                errorMessage += `${key}: ${value}. `;
              }
            });
          }
        } else if (typeof err.response.data === 'string') {
          errorMessage += err.response.data;
        }
      } else {
        errorMessage += err.message || 'Erreur inconnue';
      }
      
      setError(errorMessage);
      alert(errorMessage); // Afficher l'erreur dans une alerte pour débogage
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
