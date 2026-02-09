# OctoFit Tracker Application

A comprehensive fitness tracking application built with Django REST Framework backend and React frontend, featuring user management, team competitions, activity logging, and workout recommendations.

## Overview

OctoFit Tracker is a fitness application designed for Mergington High School that helps students track their physical activities, compete in teams, and view personalized workout suggestions. The application features Marvel and DC superhero characters as test users to make fitness fun and engaging!

## Technology Stack

### Backend
- **Framework**: Django 4.1.7
- **REST API**: Django REST Framework 3.14.0
- **Database**: SQLite (with Django ORM)
- **CORS**: django-cors-headers 4.5.0
- **Authentication**: django-allauth 0.51.0

### Frontend
- **Framework**: React 18
- **Styling**: Bootstrap 5
- **Routing**: React Router DOM
- **Build Tool**: Create React App

## Features

### 1. User Management
- View all registered users
- Track individual user points
- Associate users with teams

### 2. Team Management
- Team Marvel and Team DC
- Team descriptions and total points
- Team-based competition tracking

### 3. Activity Logging
- Track different activity types (Running, Swimming, Strength Training, Cycling, Yoga)
- Record duration and points earned
- Date-based activity history

### 4. Leaderboard
- Ranked list of all users
- Team affiliation display
- Real-time points tracking
- Visual rank indicators (gold, silver, bronze)

### 5. Workout Suggestions
- Pre-defined workout plans
- Difficulty levels (Easy, Medium, Hard)
- Duration and points value
- Superhero-themed workout names

## Project Structure

```
octofit-tracker/
├── backend/
│   ├── venv/                          # Python virtual environment
│   └── octofit_tracker/               # Django project
│       ├── manage.py
│       ├── db.sqlite3                 # SQLite database
│       └── octofit_tracker/           # Django app
│           ├── models.py              # Database models
│           ├── serializers.py         # DRF serializers
│           ├── views.py               # API views
│           ├── urls.py                # URL routing
│           ├── admin.py               # Admin configuration
│           ├── settings.py            # Django settings
│           └── management/
│               └── commands/
│                   └── populate_db.py # Database population script
└── frontend/
    ├── public/
    │   └── octofitapp-small.png      # App logo
    └── src/
        ├── components/
        │   ├── Users.js               # Users component
        │   ├── Teams.js               # Teams component
        │   ├── Activities.js          # Activities component
        │   ├── Leaderboard.js         # Leaderboard component
        │   └── Workouts.js            # Workouts component
        ├── App.js                     # Main app with routing
        ├── App.css                    # Custom styling
        └── index.js                   # Entry point
```

## Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js 14+ and npm
- Git

### Backend Setup

1. Create Python virtual environment:
   ```bash
   python3 -m venv octofit-tracker/backend/venv
   ```

2. Activate virtual environment:
   ```bash
   source octofit-tracker/backend/venv/bin/activate
   ```

3. Install Python dependencies:
   ```bash
   pip install -r octofit-tracker/backend/requirements.txt
   ```

4. Run database migrations:
   ```bash
   cd octofit-tracker/backend/octofit_tracker
   python manage.py migrate
   ```

5. Populate database with test data:
   ```bash
   python manage.py populate_db
   ```

6. Start Django development server:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

### Frontend Setup

1. Install Node.js dependencies:
   ```bash
   cd octofit-tracker/frontend
   npm install
   ```

2. Set environment variable (if using GitHub Codespaces):
   ```bash
   export REACT_APP_CODESPACE_NAME=$CODESPACE_NAME
   ```

3. Start React development server:
   ```bash
   npm start
   ```

### Using VS Code Debugger

The project includes a `.vscode/launch.json` configuration with two launch options:

1. **Launch Django Backend**: Starts the Django server on port 8000
2. **Launch React Frontend**: Starts the React dev server on port 3000

Simply press F5 or use the Run and Debug panel in VS Code to launch either server.

## API Endpoints

Base URL: `http://localhost:8000` (or your Codespace URL with port 8000)

### Available Endpoints

- **API Root**: `GET /` - Lists all available endpoints
- **Users**: `GET /api/users/` - List all users
- **Teams**: `GET /api/teams/` - List all teams
- **Activities**: `GET /api/activities/` - List all activities
- **Leaderboard**: `GET /api/leaderboard/` - List leaderboard entries
- **Workouts**: `GET /api/workouts/` - List all workouts

All endpoints support standard REST operations (GET, POST, PUT, PATCH, DELETE) via Django REST Framework's ModelViewSet.

### Testing API Endpoints

```bash
# Test API root
curl http://localhost:8000/

# Get all users
curl http://localhost:8000/api/users/

# Get all teams
curl http://localhost:8000/api/teams/

# Get leaderboard
curl http://localhost:8000/api/leaderboard/
```

## Test Data

The application comes pre-populated with superhero characters:

### Team Marvel
- Tony Stark (Iron Man)
- Steve Rogers (Captain America)
- Natasha Romanoff (Black Widow)
- Bruce Banner (Hulk)
- Thor Odinson

### Team DC
- Bruce Wayne (Batman)
- Clark Kent (Superman)
- Diana Prince (Wonder Woman)
- Barry Allen (The Flash)
- Arthur Curry (Aquaman)

Each user has:
- Activity history spanning 5 days
- Points earned from various activities
- Team affiliation

## Configuration

### Django Settings

Key settings in `octofit_tracker/settings.py`:

```python
# CORS Configuration
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = ['*']
CORS_ALLOW_HEADERS = ['*']

# Codespace support
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
if os.environ.get('CODESPACE_NAME'):
    ALLOWED_HOSTS.append(f"{os.environ.get('CODESPACE_NAME')}-8000.app.github.dev")
```

### React Environment Variables

The React app uses the `REACT_APP_CODESPACE_NAME` environment variable to determine the API base URL:

```javascript
const codespace = process.env.REACT_APP_CODESPACE_NAME;
const baseUrl = codespace 
  ? `https://${codespace}-8000.app.github.dev`
  : 'http://localhost:8000';
```

## Features Showcase

### Users Page
- Displays all registered users in a responsive table
- Shows name, email, team ID, and total points
- Bootstrap styling with hover effects

### Teams Page
- Card-based layout for each team
- Team descriptions and total points
- Creation date tracking

### Activities Page
- Comprehensive activity log
- Activity type badges with color coding
- Duration and points earned tracking
- Date-sorted display

### Leaderboard Page
- Rank-based user display
- Special badges for top 3 positions (gold, silver, bronze)
- Team affiliation shown for each user
- Real-time points display

### Workouts Page
- Card-based workout suggestions
- Difficulty level indicators (color-coded)
- Estimated duration and points value
- Superhero-themed workout names

## Development Notes

### Django Models

The application uses 5 main models:

1. **User**: User information and points tracking
2. **Team**: Team information and total points
3. **Activity**: Individual activity logs
4. **Leaderboard**: Calculated leaderboard entries
5. **Workout**: Pre-defined workout suggestions

### React Components

Each component follows a consistent pattern:

1. State management with `useState`
2. Data fetching with `useEffect`
3. Loading and error states
4. Bootstrap styling
5. Console logging for debugging

### CORS Configuration

The backend is configured to allow all origins for development. For production, update the CORS settings to only allow specific origins:

```python
CORS_ALLOWED_ORIGINS = [
    "https://your-production-domain.com",
]
```

## Troubleshooting

### Backend Issues

1. **Port 8000 already in use**:
   ```bash
   # Find and kill the process
   lsof -ti:8000 | xargs kill -9
   ```

2. **Database migrations not applied**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **No data in database**:
   ```bash
   python manage.py populate_db
   ```

### Frontend Issues

1. **Port 3000 already in use**:
   ```bash
   # Find and kill the process
   lsof -ti:3000 | xargs kill -9
   ```

2. **API connection errors**:
   - Check that Django backend is running
   - Verify CORS settings in Django
   - Check REACT_APP_CODESPACE_NAME environment variable

3. **Blank page or component not loading**:
   - Check browser console for errors
   - Verify API endpoint URLs in components
   - Ensure data format matches component expectations

## Future Enhancements

Potential features for future development:

1. **User Authentication**: Add login/logout functionality
2. **Activity Logging**: Allow users to create new activities
3. **Workout Completion**: Track completed workouts
4. **Team Statistics**: Add team performance analytics
5. **Progress Charts**: Visualize user progress over time
6. **Mobile App**: React Native mobile version
7. **Social Features**: Comments, likes, and user interactions
8. **Gamification**: Badges, achievements, and challenges

## Contributing

This is an educational project for the GitHub Copilot Agent Mode skills course. Feel free to extend and improve the application!

## License

MIT License - See LICENSE file for details

## Acknowledgments

- GitHub Copilot for AI-assisted development
- Mergington High School fitness program
- Marvel and DC Comics for character inspiration
- Bootstrap team for the excellent CSS framework
- Django and React communities

---

Built with ❤️ using GitHub Copilot Agent Mode
