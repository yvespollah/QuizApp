import React, { useState, useEffect } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import axios from 'axios';

const QuizDetail = () => {
  const { quizId } = useParams();
  const navigate = useNavigate();
  const [quiz, setQuiz] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchQuizDetails = async () => {
      try {
        setLoading(true);
        const response = await axios.get(`/quizzes/quizzes/${quizId}/`);
        setQuiz(response.data);
        setError(null);
      } catch (err) {
        console.error('Error fetching quiz details:', err);
        setError('Failed to load quiz details. Please try again later.');
      } finally {
        setLoading(false);
      }
    };

    fetchQuizDetails();
  }, [quizId]);

  const handleStartQuiz = async () => {
    try {
      // Start a new quiz attempt
      const response = await axios.post(`/quizzes/quizzes/${quizId}/start/`);
      const attemptId = response.data.id;
      
      // Navigate to the quiz taking page
      navigate(`/take-quiz/${quizId}?attempt=${attemptId}`);
    } catch (err) {
      console.error('Error starting quiz:', err);
      setError('Failed to start quiz. Please try again later.');
    }
  };

  // Function to get difficulty badge color
  const getDifficultyColor = (difficulty) => {
    switch (difficulty) {
      case 'easy':
        return 'bg-green-100 text-green-800';
      case 'medium':
        return 'bg-yellow-100 text-yellow-800';
      case 'hard':
        return 'bg-red-100 text-red-800';
      default:
        return 'bg-gray-100 text-gray-800';
    }
  };

  return (
    <div className="max-w-4xl mx-auto">
      {/* Loading state */}
      {loading ? (
        <div className="flex justify-center items-center h-64">
          <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-primary-500"></div>
        </div>
      ) : (
        <>
          {/* Error message */}
          {error ? (
            <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
              {error}
            </div>
          ) : (
            quiz && (
              <div className="bg-white rounded-lg shadow-md overflow-hidden">
                <div className="p-6">
                  <div className="flex justify-between items-start mb-4">
                    <h1 className="text-3xl font-bold text-primary-800">{quiz.title}</h1>
                    <span className={`px-3 py-1 rounded-full text-sm font-medium ${getDifficultyColor(quiz.difficulty)}`}>
                      {quiz.difficulty.charAt(0).toUpperCase() + quiz.difficulty.slice(1)}
                    </span>
                  </div>
                  
                  <p className="text-gray-600 mb-6">{quiz.description}</p>
                  
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
                    <div className="bg-gray-50 p-4 rounded-lg">
                      <h3 className="text-sm font-medium text-gray-500 mb-1">Subject</h3>
                      <p className="text-lg font-semibold">{quiz.subject}</p>
                    </div>
                    <div className="bg-gray-50 p-4 rounded-lg">
                      <h3 className="text-sm font-medium text-gray-500 mb-1">Questions</h3>
                      <p className="text-lg font-semibold">{quiz.question_count}</p>
                    </div>
                    <div className="bg-gray-50 p-4 rounded-lg">
                      <h3 className="text-sm font-medium text-gray-500 mb-1">Time Limit</h3>
                      <p className="text-lg font-semibold">
                        {quiz.time_limit ? `${quiz.time_limit} minutes` : 'No time limit'}
                      </p>
                    </div>
                  </div>
                  
                  <div className="border-t border-gray-200 pt-6">
                    <h2 className="text-xl font-semibold mb-4">About This Quiz</h2>
                    <p className="text-gray-600 mb-6">
                      This quiz contains {quiz.question_count} multiple-choice questions on {quiz.subject}.
                      After completing the quiz, you'll receive your score and AI-generated explanations for each question.
                    </p>
                    
                    <div className="flex flex-col md:flex-row justify-between items-center space-y-4 md:space-y-0">
                      <Link
                        to="/quizzes"
                        className="text-primary-600 hover:text-primary-800 font-medium"
                      >
                        ← Back to Quizzes
                      </Link>
                      <button
                        onClick={handleStartQuiz}
                        className="bg-primary-600 hover:bg-primary-700 text-white py-3 px-6 rounded-md transition duration-300"
                      >
                        Start Quiz
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            )
          )}
        </>
      )}
    </div>
  );
};

export default QuizDetail;
