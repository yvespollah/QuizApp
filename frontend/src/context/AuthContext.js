import React, { createContext, useState, useEffect } from 'react';
import axios from 'axios';
import Notification from '../components/Notification';

// Create context
const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [loading, setLoading] = useState(true);
  const [notification, setNotification] = useState({ message: null, type: null });
  const [error, setError] = useState(null);

  // Check if user is logged in on initial load
  useEffect(() => {
    const checkLoggedIn = async () => {
      // Check if token exists in local storage
      const token = localStorage.getItem('token');
      
      if (token) {
        // Load user data - Version optimisée pour la production
        const loadUser = async () => {
          if (localStorage.token) {
            setAuthToken(localStorage.token);
          } else {
            setLoading(false);
            return; // Pas de token, pas besoin de charger l'utilisateur
          }
          
          try {
            // Utiliser le chemin complet pour l'API en production
            const endpoint = process.env.NODE_ENV === 'production' 
              ? '/api/users/profile/' 
              : '/users/profile/';
            
            const res = await axios.get(endpoint);
            setUser(res.data);
            setIsAuthenticated(true);
            setLoading(false);
          } catch (err) {
            console.error('Erreur de chargement utilisateur:', err);
            localStorage.removeItem('token'); // Supprimer le token invalide
            setAuthToken(null);
            setUser(null);
            setIsAuthenticated(false);
            setLoading(false);
          }
        };
        
        loadUser();
      } else {
        setLoading(false);
      }
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

  // Register user - Version optimisée pour la production
  const register = async (userData) => {
    try {
      console.log('Tentative d\'inscription avec:', userData);
      setError(null);
      setNotification({ message: null, type: null });
      
      // Utiliser le chemin complet pour l'API en production
      const endpoint = process.env.NODE_ENV === 'production' 
        ? '/api/users/register/' 
        : '/users/register/';
      
      const res = await axios.post(endpoint, {
        username: userData.username,
        email: userData.email,
        password: userData.password,
        password2: userData.password2,
        bio: userData.bio || ''
      });
      
      console.log('Réponse d\'inscription:', res.data);
      
      // Afficher une notification de succès
      setNotification({
        message: 'Inscription réussie! Vous allez être redirigé vers la page de connexion.',
        type: 'success'
      });
      
      // Rediriger vers la page de connexion après 2 secondes
      setTimeout(() => {
        window.location.href = '/login';
      }, 2000);
      
      return res.data;
    } catch (err) {
      console.error('Erreur d\'inscription complète:', err);
      
      let message = 'L\'inscription a échoué. Vérifiez votre connexion internet.';
      
      if (err.response) {
        console.log('Données d\'erreur:', err.response.data);
        if (typeof err.response.data === 'object') {
          // Simplifier le message d'erreur
          message = Object.keys(err.response.data)
            .map(key => {
              const value = err.response.data[key];
              return `${key}: ${Array.isArray(value) ? value.join(', ') : value}`;
            })
            .join(', ');
        } else if (typeof err.response.data === 'string') {
          message = err.response.data;
        }
      } else if (err.request) {
        // La requête a été faite mais pas de réponse
        message = 'Erreur réseau: Impossible de contacter le serveur';
      } else {
        // Erreur lors de la configuration de la requête
        message = err.message || 'Erreur inconnue';
      }
      
      setError(message);
      setNotification({
        message: message,
        type: 'error'
      });
    }
  };

  // Login user - Version optimisée pour la production
  const login = async (userData) => {
    try {
      console.log('Tentative de connexion avec:', userData);
      setError(null);
      setNotification({ message: null, type: null });
      
      // Utiliser le chemin complet pour l'API en production
      const endpoint = process.env.NODE_ENV === 'production' 
        ? '/api/token/' 
        : '/token/';
      
      const res = await axios.post(endpoint, {
        email: userData.email,
        password: userData.password
      });
      
      console.log('Réponse de connexion:', res.data);
      
      // Save token to local storage
      localStorage.setItem('token', res.data.access);
      
      // Set auth token in headers
      setAuthToken(res.data.access);
      
      // Get user data
      try {
        // Utiliser le chemin complet pour l'API en production
        const profileEndpoint = process.env.NODE_ENV === 'production' 
          ? '/api/users/profile/' 
          : '/users/profile/';
        
        const userRes = await axios.get(profileEndpoint);
        console.log('Données utilisateur:', userRes.data);
        setUser(userRes.data);
        setIsAuthenticated(true);
        setError(null);
        
        // Afficher une notification de succès
        setNotification({
          message: `Connexion réussie! Bienvenue, ${userRes.data.username}.`,
          type: 'success'
        });
        
        // Rediriger vers la page d'accueil après 2 secondes
        setTimeout(() => {
          window.location.href = '/';
        }, 2000);
      } catch (profileErr) {
        console.error('Erreur profil:', profileErr);
        setIsAuthenticated(true);
        
        // Afficher une notification de succès
        setNotification({
          message: 'Connexion réussie!',
          type: 'success'
        });
        
        // Rediriger vers la page d'accueil après 2 secondes
        setTimeout(() => {
          window.location.href = '/';
        }, 2000);
      }
      
      return res.data;
    } catch (err) {
      console.error('Erreur de connexion complète:', err);
      
      let message = 'Échec de connexion. Vérifiez vos identifiants.';
      
      if (err.response) {
        console.log('Données d\'erreur:', err.response.data);
        if (typeof err.response.data === 'object') {
          if (err.response.data.detail) {
            message = err.response.data.detail;
          } else {
            // Simplifier le message d'erreur
            message = Object.keys(err.response.data)
              .map(key => {
                const value = err.response.data[key];
                return `${key}: ${Array.isArray(value) ? value.join(', ') : value}`;
              })
              .join(', ');
          }
        } else if (typeof err.response.data === 'string') {
          message = err.response.data;
        }
      } else if (err.request) {
        // La requête a été faite mais pas de réponse
        message = 'Erreur réseau: Impossible de contacter le serveur';
      } else {
        // Erreur lors de la configuration de la requête
        message = err.message || 'Erreur inconnue';
      }
      
      setError(message);
      setNotification({
        message: message,
        type: 'error'
      });
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

  // Clear errors and notifications
  const clearNotifications = () => {
    setError(null);
    setNotification({ message: null, type: null });
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        isAuthenticated,
        loading,
        error,
        notification,
        register,
        login,
        logout,
        updateProfile,
        clearNotifications
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
