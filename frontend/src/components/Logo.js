import React from 'react';
import logoImage from '../assets/logo.png';

const Logo = () => {
  return (
    <div className="flex items-center">
      <img src={logoImage} alt="Yves Programmeur Logo" className="h-16 md:h-15" />
    </div>
  );
};

export default Logo;
