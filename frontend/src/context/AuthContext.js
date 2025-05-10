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
      const res = await axios.post('/users/register/', userData);
      return res.data;
    } catch (err) {
      setError(err.response?.data?.detail || 'Registration failed');
      throw err;
    }
  };

  // Login user
  const login = async (userData) => {
    try {
      const res = await axios.post('/token/', userData);
      
      // Save token to local storage
      localStorage.setItem('token', res.data.access);
      
      // Set auth token in headers
      setAuthToken(res.data.access);
      
      // Get user data
      const userRes = await axios.get('/users/profile/');
      setUser(userRes.data);
      setIsAuthenticated(true);
      setError(null);
      
      return res.data;
    } catch (err) {
      setError(err.response?.data?.detail || 'Login failed');
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
