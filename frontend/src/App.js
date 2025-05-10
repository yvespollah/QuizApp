import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import axios from 'axios';

// Components
import Navbar from './components/Navbar';
import Footer from './components/Footer';

// Pages
import Home from './pages/Home';
import Login from './pages/Login';
import Register from './pages/Register';
import Profile from './pages/Profile';
import QuizList from './pages/QuizList';
import QuizDetail from './pages/QuizDetail';
import TakeQuiz from './pages/TakeQuiz';
import QuizResults from './pages/QuizResults';
import QuizHistory from './pages/QuizHistory';

// Context
import { AuthProvider } from './context/AuthContext';

// Set up axios defaults
const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';
axios.defaults.baseURL = API_URL;
axios.defaults.headers.post['Content-Type'] = 'application/json';

function App() {
  return (
    <AuthProvider>
      <Router>
        <div className="flex flex-col min-h-screen">
          <Navbar />
          <main className="flex-grow container mx-auto px-4 py-8">
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/login" element={<Login />} />
              <Route path="/register" element={<Register />} />
              <Route path="/profile" element={
                <PrivateRoute>
                  <Profile />
                </PrivateRoute>
              } />
              <Route path="/quizzes" element={
                <PrivateRoute>
                  <QuizList />
                </PrivateRoute>
              } />
              <Route path="/quizzes/:quizId" element={
                <PrivateRoute>
                  <QuizDetail />
                </PrivateRoute>
              } />
              <Route path="/take-quiz/:quizId" element={
                <PrivateRoute>
                  <TakeQuiz />
                </PrivateRoute>
              } />
              <Route path="/quiz-results/:attemptId" element={
                <PrivateRoute>
                  <QuizResults />
                </PrivateRoute>
              } />
              <Route path="/history" element={
                <PrivateRoute>
                  <QuizHistory />
                </PrivateRoute>
              } />
            </Routes>
          </main>
          <Footer />
        </div>
      </Router>
    </AuthProvider>
  );
}

// Private route component
function PrivateRoute({ children }) {
  const { isAuthenticated, loading } = React.useContext(AuthProvider.context);
  
  if (loading) {
    return <div className="flex justify-center items-center h-64">
      <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-primary-500"></div>
    </div>;
  }
  
  return isAuthenticated ? children : <Navigate to="/login" />;
}

export default App;
