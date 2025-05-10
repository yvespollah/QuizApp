import React from 'react';

const Logo = () => {
  return (
    <div className="flex items-center">
      <div className="flex h-10 w-10 relative mr-2">
        <div className="absolute top-0 left-0 w-5 h-5 bg-yellow-400 rounded-tl-full"></div>
        <div className="absolute top-0 right-0 w-5 h-5 bg-pink-500 rounded-tr-full"></div>
        <div className="absolute bottom-0 left-0 w-5 h-5 bg-black rounded-bl-full"></div>
        <div className="absolute bottom-0 right-0 w-5 h-5 bg-green-400 rounded-br-full"></div>
      </div>
      <div className="font-bold text-lg">
        <span className="text-blue-800">Yves</span>
        <span className="block text-blue-900">Programmeur</span>
      </div>
    </div>
  );
};

export default Logo;
