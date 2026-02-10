# OctoFit Tracker

A comprehensive fitness tracking application built with Django REST Framework and React.

## Features

- **User Authentication**: Secure user registration and login
- **Activity Logging**: Track various fitness activities (running, cycling, swimming, etc.)
- **Team Management**: Create and join fitness teams
- **Competitive Leaderboard**: See rankings by daily, weekly, or monthly periods
- **Personalized Workouts**: Get workout suggestions based on your fitness level

## Tech Stack

### Backend
- Django 4.1.7
- Django REST Framework
- SQLite/MongoDB (Djongo)
- django-allauth for authentication
- django-cors-headers for CORS support

### Frontend
- React 18
- React Router DOM
- Bootstrap 5
- Axios (for API calls)

## Project Structure

```
octofit-tracker/
├── backend/
│   ├── octofit_tracker/     # Django project settings
│   ├── users/               # User profiles app
│   ├── activities/          # Activity tracking app
│   ├── teams/               # Team management app
│   ├── leaderboard/         # Leaderboard app
│   ├── workouts/            # Workout suggestions app
│   ├── venv/                # Python virtual environment
│   └── requirements.txt     # Python dependencies
└── frontend/
    ├── public/              # Static files
    ├── src/
    │   ├── components/      # React components
    │   └── App.js           # Main App component
    └── package.json         # Node dependencies
```

## Setup Instructions

### Backend Setup

1. Create and activate virtual environment:
```bash
python3 -m venv octofit-tracker/backend/venv
source octofit-tracker/backend/venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r octofit-tracker/backend/requirements.txt
```

3. Run migrations:
```bash
cd octofit-tracker/backend
python manage.py migrate
```

4. Create a superuser:
```bash
python manage.py createsuperuser
```

5. Start the development server:
```bash
python manage.py runserver 0.0.0.0:8000
```

The API will be available at `http://localhost:8000/api/`

### Frontend Setup

1. Install dependencies:
```bash
cd octofit-tracker/frontend
npm install
```

2. Start the development server:
```bash
npm start
```

The frontend will be available at `http://localhost:3000`

## API Endpoints

- `/api/` - API root with endpoint listing
- `/api/users/` - User management
- `/api/profiles/` - User profiles
- `/api/activities/` - Activity tracking
- `/api/teams/` - Team management
- `/api/leaderboard/` - Leaderboard data
- `/api/workout-suggestions/` - Workout suggestions
- `/api/user-workouts/` - User workout tracking
- `/api/auth/login/` - User login
- `/api/auth/logout/` - User logout
- `/api/auth/registration/` - User registration
- `/admin/` - Django admin panel

## Development

### Backend
The backend uses Django REST Framework with ViewSets for each app. Models are defined for:
- UserProfile (users app)
- Activity (activities app)
- Team (teams app)
- LeaderboardEntry (leaderboard app)
- WorkoutSuggestion and UserWorkout (workouts app)

### Frontend
The frontend uses React with functional components and hooks. Main components:
- Home: Landing page with feature overview
- Activities: Activity logging and tracking
- Teams: Team creation and management
- Leaderboard: Competitive rankings
- Workouts: Personalized workout suggestions

## Configuration

### CORS Settings
The backend is configured to allow requests from `http://localhost:3000` (development) and GitHub Codespaces environments.

### Database
Currently configured to use SQLite for development. For production, configure MongoDB using the djongo engine in `settings.py`.

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
