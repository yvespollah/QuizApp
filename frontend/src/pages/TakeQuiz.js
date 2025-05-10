import React, { useState, useEffect } from 'react';
import { useParams, useNavigate, useLocation } from 'react-router-dom';
import axios from 'axios';

const TakeQuiz = () => {
  const { quizId } = useParams();
  const navigate = useNavigate();
  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);
  const attemptId = queryParams.get('attempt');

  const [quiz, setQuiz] = useState(null);
  const [attempt, setAttempt] = useState(null);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [answers, setAnswers] = useState({});
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState(null);
  const [timeLeft, setTimeLeft] = useState(null);

  // Fetch quiz details and create/get attempt
  useEffect(() => {
    const fetchQuizAndAttempt = async () => {
      try {
        setLoading(true);
        
        // Fetch quiz details
        const quizResponse = await axios.get(`/quizzes/quizzes/${quizId}/`);
        setQuiz(quizResponse.data);
        
        // Get or create attempt
        let attemptResponse;
        if (attemptId) {
          attemptResponse = await axios.get(`/quizzes/attempts/${attemptId}/`);
        } else {
          attemptResponse = await axios.post(`/quizzes/quizzes/${quizId}/start/`);
        }
        
        setAttempt(attemptResponse.data);
        
        // Initialize time left if quiz has a time limit
        if (quizResponse.data.time_limit) {
          const startTime = new Date(attemptResponse.data.started_at);
          const endTime = new Date(startTime.getTime() + quizResponse.data.time_limit * 60000);
          const now = new Date();
          const timeLeftMs = endTime - now;
          
          if (timeLeftMs > 0) {
            setTimeLeft(Math.floor(timeLeftMs / 1000));
          } else {
            // Time's up, submit the quiz
            handleSubmitQuiz();
          }
        }
        
        // Initialize answers from existing attempt answers
        if (attemptResponse.data.answers && attemptResponse.data.answers.length > 0) {
          const answerMap = {};
          attemptResponse.data.answers.forEach(answer => {
            answerMap[answer.question] = answer.selected_choice;
          });
          setAnswers(answerMap);
        }
        
        setError(null);
      } catch (err) {
        console.error('Error fetching quiz or attempt:', err);
        setError('Failed to load quiz. Please try again later.');
      } finally {
        setLoading(false);
      }
    };

    fetchQuizAndAttempt();
  }, [quizId, attemptId]);

  // Timer effect
  useEffect(() => {
    if (timeLeft === null || timeLeft <= 0) return;
    
    const timer = setInterval(() => {
      setTimeLeft(prev => {
        if (prev <= 1) {
          clearInterval(timer);
          // Time's up, submit the quiz
          handleSubmitQuiz();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);
    
    return () => clearInterval(timer);
  }, [timeLeft]);

  // Format time left as mm:ss
  const formatTimeLeft = () => {
    if (timeLeft === null) return '';
    
    const minutes = Math.floor(timeLeft / 60);
    const seconds = timeLeft % 60;
    return `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
  };

  const handleAnswerSelect = async (questionId, choiceId) => {
    // Update local state
    setAnswers(prev => ({
      ...prev,
      [questionId]: choiceId
    }));
    
    try {
      // Submit answer to backend
      await axios.post(`/quizzes/attempts/${attempt.id}/submit_answer/`, {
        question_id: questionId,
        choice_id: choiceId
      });
    } catch (err) {
      console.error('Error submitting answer:', err);
      // We don't show an error to the user here to avoid disrupting the quiz flow
      // The answer will still be saved locally and submitted with the final submission
    }
  };

  const handleNextQuestion = () => {
    if (currentQuestionIndex < quiz.questions.length - 1) {
      setCurrentQuestionIndex(prev => prev + 1);
    }
  };

  const handlePreviousQuestion = () => {
    if (currentQuestionIndex > 0) {
      setCurrentQuestionIndex(prev => prev - 1);
    }
  };

  const handleSubmitQuiz = async () => {
    if (submitting) return;
    
    try {
      setSubmitting(true);
      
      // Submit the quiz
      const response = await axios.post(`/quizzes/attempts/${attempt.id}/complete/`);
      
      // Navigate to results page
      navigate(`/quiz-results/${attempt.id}`);
    } catch (err) {
      console.error('Error submitting quiz:', err);
      setError('Failed to submit quiz. Please try again.');
      setSubmitting(false);
    }
  };

  // Get current question
  const currentQuestion = quiz?.questions?.[currentQuestionIndex];

  // Calculate progress percentage
  const progressPercentage = quiz?.questions?.length 
    ? Math.round(((currentQuestionIndex + 1) / quiz.questions.length) * 100) 
    : 0;

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
            quiz && attempt && (
              <div className="bg-white rounded-lg shadow-md overflow-hidden">
                {/* Quiz header */}
                <div className="bg-primary-700 text-white p-4">
                  <div className="flex justify-between items-center">
                    <h1 className="text-xl font-bold">{quiz.title}</h1>
                    {timeLeft !== null && (
                      <div className="bg-white text-primary-800 px-3 py-1 rounded-md font-mono font-bold">
                        {formatTimeLeft()}
                      </div>
                    )}
                  </div>
                  
                  {/* Progress bar */}
                  <div className="mt-4 bg-primary-600 rounded-full h-2.5">
                    <div 
                      className="bg-white h-2.5 rounded-full" 
                      style={{ width: `${progressPercentage}%` }}
                    ></div>
                  </div>
                  <div className="mt-1 text-sm text-primary-200">
                    Question {currentQuestionIndex + 1} of {quiz.questions.length}
                  </div>
                </div>
                
                {/* Question content */}
                {currentQuestion && (
                  <div className="p-6">
                    <h2 className="text-xl font-semibold mb-6">{currentQuestion.text}</h2>
                    
                    {/* Answer choices */}
                    <div className="space-y-3 mb-8">
                      {currentQuestion.choices.map(choice => (
                        <div 
                          key={choice.id}
                          className={`border rounded-lg p-4 cursor-pointer transition-colors ${
                            answers[currentQuestion.id] === choice.id
                              ? 'border-primary-500 bg-primary-50'
                              : 'border-gray-300 hover:border-primary-300'
                          }`}
                          onClick={() => handleAnswerSelect(currentQuestion.id, choice.id)}
                        >
                          <div className="flex items-center">
                            <div className={`w-5 h-5 rounded-full border flex items-center justify-center mr-3 ${
                              answers[currentQuestion.id] === choice.id
                                ? 'border-primary-500 bg-primary-500'
                                : 'border-gray-400'
                            }`}>
                              {answers[currentQuestion.id] === choice.id && (
                                <div className="w-2 h-2 rounded-full bg-white"></div>
                              )}
                            </div>
                            <span>{choice.text}</span>
                          </div>
                        </div>
                      ))}
                    </div>
                    
                    {/* Navigation buttons */}
                    <div className="flex justify-between">
                      <button
                        onClick={handlePreviousQuestion}
                        disabled={currentQuestionIndex === 0}
                        className={`px-4 py-2 rounded-md ${
                          currentQuestionIndex === 0
                            ? 'bg-gray-200 text-gray-500 cursor-not-allowed'
                            : 'bg-gray-200 text-gray-800 hover:bg-gray-300'
                        }`}
                      >
                        Previous
                      </button>
                      
                      {currentQuestionIndex < quiz.questions.length - 1 ? (
                        <button
                          onClick={handleNextQuestion}
                          className="bg-primary-600 hover:bg-primary-700 text-white px-4 py-2 rounded-md"
                        >
                          Next
                        </button>
                      ) : (
                        <button
                          onClick={handleSubmitQuiz}
                          disabled={submitting}
                          className="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded-md"
                        >
                          {submitting ? 'Submitting...' : 'Submit Quiz'}
                        </button>
                      )}
                    </div>
                  </div>
                )}
                
                {/* Question navigation */}
                <div className="bg-gray-100 p-4 border-t border-gray-200">
                  <div className="flex flex-wrap gap-2">
                    {quiz.questions.map((question, index) => (
                      <button
                        key={question.id}
                        onClick={() => setCurrentQuestionIndex(index)}
                        className={`w-8 h-8 rounded-full flex items-center justify-center text-sm font-medium ${
                          index === currentQuestionIndex
                            ? 'bg-primary-600 text-white'
                            : answers[question.id]
                              ? 'bg-primary-200 text-primary-800'
                              : 'bg-white text-gray-700 border border-gray-300'
                        }`}
                      >
                        {index + 1}
                      </button>
                    ))}
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

export default TakeQuiz;
