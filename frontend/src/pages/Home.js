import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import AuthContext from '../context/AuthContext';

const Home = () => {
  const { isAuthenticated } = useContext(AuthContext);

  return (
    <div className="max-w-4xl mx-auto">
      <div className="text-center py-10">
        <h1 className="text-4xl md:text-5xl font-bold mb-6 text-primary-800">
          Welcome to my Quiz App
        </h1>
        <p className="text-xl text-gray-600 mb-8">
          Test your knowledge with interactive quizzes and get AI-powered explanations
        </p>

        {isAuthenticated ? (
          <div className="space-x-4">
            <Link
              to="/quizzes"
              className="bg-primary-600 hover:bg-primary-700 text-white font-bold py-3 px-6 rounded-lg transition duration-300 inline-block"
            >
              Browse Quizzes
            </Link>
            <Link
              to="/history"
              className="bg-gray-200 hover:bg-gray-300 text-gray-800 font-bold py-3 px-6 rounded-lg transition duration-300 inline-block"
            >
              View History
            </Link>
          </div>
        ) : (
          <div className="space-x-4">
            <Link
              to="/login"
              className="bg-primary-600 hover:bg-primary-700 text-white font-bold py-3 px-6 rounded-lg transition duration-300 inline-block"
            >
              Login
            </Link>
            <Link
              to="/register"
              className="bg-gray-200 hover:bg-gray-300 text-gray-800 font-bold py-3 px-6 rounded-lg transition duration-300 inline-block"
            >
              Register
            </Link>
          </div>
        )}
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12">
        <FeatureCard
          title="Multiple Choice Quizzes"
          description="Test your knowledge with our carefully crafted multiple-choice quizzes on various subjects."
          icon={
            <svg className="w-12 h-12 text-primary-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
          }
        />
        <FeatureCard
          title="AI-Powered Explanations"
          description="Get detailed explanations for your answers powered by artificial intelligence."
          icon={
            <svg className="w-12 h-12 text-primary-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"></path>
            </svg>
          }
        />
        <FeatureCard
          title="Track Your Progress"
          description="Keep track of your quiz history and see how you've improved over time."
          icon={
            <svg className="w-12 h-12 text-primary-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path>
            </svg>
          }
        />
      </div>

      <div className="bg-gray-100 rounded-lg p-8 mb-12">
        <h2 className="text-2xl font-bold mb-4 text-primary-800">How It Works</h2>
        <ol className="list-decimal list-inside space-y-4 text-gray-700">
          <li className="pl-2">
            <span className="font-semibold">Create an account</span> - Register with your email and password to get started.
          </li>
          <li className="pl-2">
            <span className="font-semibold">Browse quizzes</span> - Explore our collection of quizzes on various subjects and difficulty levels.
          </li>
          <li className="pl-2">
            <span className="font-semibold">Take a quiz</span> - Answer multiple-choice questions within the time limit.
          </li>
          <li className="pl-2">
            <span className="font-semibold">Get AI explanations</span> - After submitting, receive detailed explanations for each question.
          </li>
          <li className="pl-2">
            <span className="font-semibold">Track progress</span> - Review your quiz history and see your improvement over time.
          </li>
        </ol>
      </div>
    </div>
  );
};

// Feature card component
const FeatureCard = ({ title, description, icon }) => {
  return (
    <div className="bg-white rounded-lg shadow-md p-6 transition duration-300 hover:shadow-lg">
      <div className="flex justify-center mb-4">{icon}</div>
      <h3 className="text-xl font-semibold mb-2 text-center text-primary-800">{title}</h3>
      <p className="text-gray-600 text-center">{description}</p>
    </div>
  );
};

export default Home;
