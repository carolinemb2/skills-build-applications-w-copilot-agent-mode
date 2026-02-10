# OctoFit Tracker

A fitness tracking application built with Django REST Framework and React for Mergington High School.

## Features

- **User Profiles**: Track fitness levels and total points
- **Activity Logging**: Log various activities (running, walking, cycling, swimming, strength training, yoga)
- **Team Management**: Create and join teams for group competitions
- **Leaderboard**: View rankings based on points earned from activities
- **Workout Suggestions**: Get personalized workout recommendations

## Technology Stack

- **Backend**: Python 3.12, Django 4.2.26, Django REST Framework 3.14.0
- **Frontend**: React 18, Bootstrap 5, React Router
- **Database**: SQLite (for development)

> **Note**: The application uses SQLite as the database. Previous MongoDB support via djongo has been removed due to dependency conflicts with security updates.

## Project Structure

```
octofit-tracker/
├── backend/
│   ├── fitness/              # Main Django app
│   │   ├── models.py         # Database models
│   │   ├── serializers.py    # API serializers
│   │   ├── views.py          # API views
│   │   └── admin.py          # Admin interface
│   ├── octofit_tracker/      # Django project settings
│   ├── manage.py
│   └── requirements.txt
└── frontend/
    ├── src/
    │   ├── components/       # React components
    │   │   ├── Home.js
    │   │   ├── Activities.js
    │   │   ├── Teams.js
    │   │   └── Leaderboard.js
    │   ├── App.js
    │   └── index.js
    └── package.json
```

## Setup Instructions

### Backend Setup

1. Create and activate Python virtual environment:
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

4. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

5. Load sample data (optional):
```bash
python manage.py shell < create_sample_data.py
```

6. Start the Django development server:
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

2. Create a `.env` file (if not in Codespaces):
```bash
echo "REACT_APP_API_URL=http://localhost:8000" > .env
```

3. Start the React development server:
```bash
npm start
```

The application will be available at `http://localhost:3000`

## API Endpoints

- `GET /api/` - API root
- `GET/POST /api/activities/` - List/create activities
- `GET/POST /api/profiles/` - User profiles
- `GET/POST /api/teams/` - Teams
- `GET /api/leaderboard/` - Leaderboard rankings
- `GET /api/workout-suggestions/` - Workout suggestions

## Admin Interface

Access the Django admin interface at `http://localhost:8000/admin/` to manage:
- Users and profiles
- Activities
- Teams
- Workout suggestions

## Sample Users

The sample data includes these users:
- **paul_octo** - PE teacher (password: password123)
- **jessica_cat** - IT department head (password: password123)
- **student1** - Student (password: password123)
- **student2** - Student (password: password123)
- **admin** - Superuser (password: admin123)

## Development

### Running in GitHub Codespaces

The application is configured to work in GitHub Codespaces with proper port forwarding:
- Port 8000 (Django) - Public
- Port 3000 (React) - Public

CORS settings are automatically configured for Codespaces URLs.

### Testing the Application

1. Start both backend and frontend servers
2. Navigate to `http://localhost:3000`
3. Explore the different pages:
   - Home: Welcome page with feature overview
   - Activities: View and log fitness activities
   - Teams: Create and view teams
   - Leaderboard: View user rankings by points

## Contributing

This project was built as part of a GitHub Copilot workshop for Mergington High School.

## License

See LICENSE file for details.
