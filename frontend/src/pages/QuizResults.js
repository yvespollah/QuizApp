import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import axios from 'axios';

const QuizResults = () => {
  const { attemptId } = useParams();
  const [attempt, setAttempt] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchAttemptResults = async () => {
      try {
        setLoading(true);
        const response = await axios.get(`/quizzes/attempts/${attemptId}/`);
        setAttempt(response.data);
        setError(null);
      } catch (err) {
        console.error('Error fetching quiz results:', err);
        setError('Failed to load quiz results. Please try again later.');
      } finally {
        setLoading(false);
      }
    };

    fetchAttemptResults();
  }, [attemptId]);

  // Calculate stats
  const calculateStats = () => {
    if (!attempt || !attempt.answers) return null;
    
    const totalQuestions = attempt.answers.length;
    const correctAnswers = attempt.answers.filter(answer => answer.is_correct).length;
    const incorrectAnswers = totalQuestions - correctAnswers;
    const score = attempt.score || 0;
    
    return {
      totalQuestions,
      correctAnswers,
      incorrectAnswers,
      score
    };
  };

  const stats = calculateStats();

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
            attempt && stats && (
              <div>
                {/* Results header */}
                <div className="bg-white rounded-lg shadow-md p-6 mb-8">
                  <h1 className="text-3xl font-bold mb-6 text-center text-primary-800">Quiz Results</h1>
                  
                  <div className="flex justify-center mb-8">
                    <div className="w-48 h-48 rounded-full border-8 border-primary-100 flex items-center justify-center">
                      <div className="text-center">
                        <div className="text-4xl font-bold text-primary-600">{Math.round(stats.score)}%</div>
                        <div className="text-gray-500 mt-2">Your Score</div>
                      </div>
                    </div>
                  </div>
                  
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
                    <div className="bg-gray-50 p-4 rounded-lg text-center">
                      <div className="text-2xl font-bold text-gray-800">{stats.totalQuestions}</div>
                      <div className="text-gray-500">Total Questions</div>
                    </div>
                    <div className="bg-green-50 p-4 rounded-lg text-center">
                      <div className="text-2xl font-bold text-green-600">{stats.correctAnswers}</div>
                      <div className="text-green-600">Correct Answers</div>
                    </div>
                    <div className="bg-red-50 p-4 rounded-lg text-center">
                      <div className="text-2xl font-bold text-red-600">{stats.incorrectAnswers}</div>
                      <div className="text-red-600">Incorrect Answers</div>
                    </div>
                  </div>
                  
                  <div className="flex justify-center">
                    <Link
                      to="/quizzes"
                      className="bg-primary-600 hover:bg-primary-700 text-white py-2 px-6 rounded-md transition duration-300"
                    >
                      Back to Quizzes
                    </Link>
                  </div>
                </div>
                
                {/* Detailed answers */}
                <h2 className="text-2xl font-bold mb-4 text-primary-800">Detailed Results</h2>
                
                <div className="space-y-6">
                  {attempt.answers.map((answer, index) => (
                    <div 
                      key={answer.id} 
                      className="bg-white rounded-lg shadow-md overflow-hidden"
                    >
                      <div className={`p-4 ${answer.is_correct ? 'bg-green-50' : 'bg-red-50'}`}>
                        <div className="flex items-start">
                          <div className={`flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center mr-3 ${
                            answer.is_correct ? 'bg-green-500' : 'bg-red-500'
                          } text-white font-bold`}>
                            {answer.is_correct ? '✓' : '✗'}
                          </div>
                          <div>
                            <h3 className="text-lg font-semibold">Question {index + 1}</h3>
                            <p className="text-gray-700">{answer.question_text}</p>
                          </div>
                        </div>
                      </div>
                      
                      <div className="p-4 border-t border-gray-200">
                        <div className="mb-4">
                          <div className="text-sm font-medium text-gray-500 mb-1">Your Answer:</div>
                          <div className={`py-2 px-3 rounded ${
                            answer.is_correct ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'
                          }`}>
                            {answer.selected_choice_text}
                          </div>
                        </div>
                        
                        {!answer.is_correct && (
                          <div className="mb-4">
                            <div className="text-sm font-medium text-gray-500 mb-1">Correct Answer:</div>
                            <div className="bg-green-100 text-green-800 py-2 px-3 rounded">
                              {answer.correct_choice}
                            </div>
                          </div>
                        )}
                        
                        <div>
                          <div className="text-sm font-medium text-gray-500 mb-1">AI Explanation:</div>
                          <div className="bg-gray-50 p-3 rounded border border-gray-200 text-gray-700">
                            {answer.ai_explanation || "No explanation available."}
                          </div>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )
          )}
        </>
      )}
    </div>
  );
};

export default QuizResults;
