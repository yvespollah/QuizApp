import React from 'react';
import Logo from './Logo'; // Import du composant Logo

const Footer = () => {
  return (
    <footer className="bg-primary-700 text-white py-6">
      <div className="container mx-auto px-4">
        <div className="flex flex-col md:flex-row justify-between items-center">
          <div className="mb-4 md:mb-0 flex items-center">
            <Logo />
            <div className="ml-2">
              <h3 className="text-lg font-semibold">Quiz App</h3>
              <p className="text-sm text-primary-200">Learn with AI-powered explanations</p>
            </div>
          </div>
          
          <div className="text-sm text-primary-200">
            &copy; {new Date().getFullYear()} Yves Programmeur. All rights reserved.
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
