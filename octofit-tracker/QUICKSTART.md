# OctoFit Tracker - Quick Start Guide

## 🚀 5-Minute Setup

### Prerequisites
- Python 3.12+ installed
- Node.js 24+ and npm installed
- Terminal/Command line access

### Quick Setup

#### 1. Backend Setup (2 minutes)
```bash
# Navigate to backend directory
cd octofit-tracker/backend

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser (optional, for admin access)
python manage.py createsuperuser

# Load sample data
python manage.py shell << EOF
from django.contrib.auth.models import User
from fitness.models import UserProfile, Team, Activity, WorkoutSuggestion
from datetime import date, timedelta

# Create sample users
users_data = [
    {'username': 'paul_octo', 'email': 'paul@mergington.edu', 'password': 'password123'},
    {'username': 'jessica_cat', 'email': 'jessica@mergington.edu', 'password': 'password123'},
]

for user_data in users_data:
    user, created = User.objects.get_or_create(
        username=user_data['username'],
        defaults={'email': user_data['email']}
    )
    if created:
        user.set_password(user_data['password'])
        user.save()
        UserProfile.objects.create(user=user, fitness_level='beginner')

print("Sample data created!")
EOF

# Start Django server
python manage.py runserver 0.0.0.0:8000
```

#### 2. Frontend Setup (2 minutes)
Open a new terminal window:

```bash
# Navigate to frontend directory
cd octofit-tracker/frontend

# Install dependencies
npm install

# Create .env file
echo "REACT_APP_API_URL=http://localhost:8000" > .env

# Start React development server
npm start
```

### Access the Application
- **Frontend**: Open http://localhost:3000 in your browser
- **Backend API**: http://localhost:8000/api/
- **Admin Panel**: http://localhost:8000/admin/

### Test the Application
1. **Home Page**: See the welcome message and feature cards
2. **Activities**: Click "+ Log Activity" to create a new activity
3. **Teams**: Create a team or view existing teams
4. **Leaderboard**: See user rankings by points

### Default Credentials
- **Admin**: username: `admin`, password: `admin123` (if you created superuser)
- **Sample Users**: username: `paul_octo`, password: `password123`

## 🎯 Quick Tips

### Adding Your First Activity
1. Go to Activities page
2. Click "+ Log Activity"
3. Fill in the form:
   - Select activity type (e.g., Running)
   - Enter duration in minutes (e.g., 30)
   - Optional: Add distance and calories
   - Click "Save Activity"
4. Your activity appears with points calculated automatically!

### Creating a Team
1. Go to Teams page
2. Click "+ Create Team"
3. Enter team name and description
4. Click "Create Team"
5. Your team appears with your points!

### Viewing Rankings
1. Go to Leaderboard page
2. See all users ranked by total points
3. Top 3 users get medals 🥇🥈🥉

## 🔧 Troubleshooting

### Port Already in Use
If port 8000 or 3000 is already in use:
```bash
# For Django (backend)
python manage.py runserver 8001

# For React (frontend)
PORT=3001 npm start
# Then update .env: REACT_APP_API_URL=http://localhost:8001
```

### CORS Errors
Make sure Django is running on port 8000 and React on port 3000, or update the CORS settings in `backend/octofit_tracker/settings.py`.

### Database Errors
Delete the database and start fresh:
```bash
cd octofit-tracker/backend
rm db.sqlite3
python manage.py migrate
# Then recreate sample data
```

## 📚 Next Steps

- Read the full [README.md](README.md) for detailed information
- Check [SECURITY.md](SECURITY.md) for security guidelines
- Explore the Django admin at http://localhost:8000/admin/
- Customize the application for your needs

## 💡 Need Help?

Refer to the main README.md for comprehensive documentation including:
- Detailed API documentation
- Component descriptions
- Configuration options
- Deployment guidelines

Enjoy using OctoFit Tracker! 🏃‍♂️💪🏆
