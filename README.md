# Yves Programmeur Quiz App

A responsive web application that allows students to take quizzes with AI-generated explanations after submission.

## Features

- User authentication (register, login, logout)
- Quiz management (create, edit, take quizzes)
- Multiple-choice questions with scoring
- AI-powered feedback and explanations
- Responsive design for mobile and desktop

## Tech Stack

### Frontend
- React.js
- Tailwind CSS
- Axios for API calls
- React Router for navigation

### Backend
- Django
- Django REST Framework
- Simple JWT for authentication
- SQLite database
- Hugging Face Transformers for AI explanations

## Setup Instructions

### Backend Setup
1. Navigate to the `backend` directory
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Create a superuser: `python manage.py createsuperuser`
7. Start the server: `python manage.py runserver`

### Frontend Setup
1. Navigate to the `frontend` directory
2. Install dependencies: `npm install`
3. Start the development server: `npm start`

## Project Structure
- `/backend` - Django REST API
- `/frontend` - React application
