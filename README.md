# Capestone

## Car Dealership Application

A full-stack car dealership management application built with Django REST Framework and React.

### Project Name
**CarDealership**

### Repository Name
**capestone**

### Tech Stack
- **Backend**: Django 4.2, Django REST Framework
- **Frontend**: React 18, React Router
- **Database**: SQLite3
- **Authentication**: Token-based (DRF Tokens)
- **CI/CD**: GitHub Actions

### Project Structure
```
capestone/
├── server/
│   ├── backend/              # Django project configuration
│   ├── dealership/           # Django app (models, views, APIs)
│   ├── frontend/             # React frontend application
│   │   ├── static/           # Static HTML pages
│   │   │   ├── About.html    # About Us page
│   │   │   ├── Contact.html  # Contact Us page
│   │   │   └── css/          # Stylesheets
│   │   └── src/              # React source code
│   │       └── components/
│   │           ├── Register/ # Registration component
│   │           ├── Login/    # Login component
│   │           ├── Home/     # Home page with dealer listings
│   │           ├── DealerDetails/ # Dealer details & reviews
│   │           └── PostReview/ # Review submission
│   ├── manage.py
│   └── requirements.txt
├── README.md
└── .github/workflows/
```

### API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/login/ | User login |
| POST | /api/logout/ | User logout |
| POST | /api/signup/ | User registration |
| GET | /api/dealers/ | Get all dealers |
| GET | /api/dealers/{id}/ | Get dealer by ID |
| GET | /api/dealers/state/{state}/ | Get dealers by state |
| GET | /api/reviews/{dealer_id}/ | Get dealer reviews |
| POST | /api/reviews/{dealer_id}/ | Post a review |
| GET | /api/carmakes/ | Get all car makes/models |
| POST | /api/analyze-review/ | Analyze review sentiment |

### Setup Instructions
1. Install Python dependencies: `pip install -r server/requirements.txt`
2. Run migrations: `python server/manage.py migrate`
3. Seed data: `python server/manage.py loaddata seed_data.json`
4. Start Django server: `python server/manage.py runserver`
5. Install frontend deps: `cd server/frontend && npm install`
6. Start React dev server: `npm start`

### Author
Santhosh Raj T
