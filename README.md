# Capestone - Car Dealership Application

## Project Name: CarDealership
## Repository Name: capestoneproject

A full-stack car dealership management application built with Django REST Framework and React.

### Tech Stack
- **Backend**: Django 5.2, Django REST Framework
- **Frontend**: React 18, React Router DOM
- **Database**: SQLite3
- **Authentication**: Session-based with Token auth
- **CI/CD**: GitHub Actions (Lint Python + Lint JavaScript)

### API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| /djangoapp/login/ | POST | User login with userName/password |
| /djangoapp/logout/ | GET | User logout |
| /djangoapp/get_cars/ | GET | Get all car makes and models |
| /djangoapp/get_dealers/ | GET | Get all 50 dealers |
| /djangoapp/fetchDealer/{id}/ | GET | Get dealer by ID |
| /djangoapp/reviews/{id}/ | GET/POST | Get/post dealer reviews |
| /djangoapp/analyze-review/ | GET | Analyze review sentiment |

### Project Structure
```
capestoneproject/
├── server/
│   ├── backend/           # Django project config
│   ├── dealership/        # Django app (models, views, APIs)
│   ├── frontend/          # React frontend
│   │   ├── static/
│   │   │   ├── About.html
│   │   │   ├── Contact.html
│   │   │   └── css/style.css
│   │   └── src/
│   │       └── components/
│   │           ├── Register/Register.jsx
│   │           ├── Login/Login.jsx
│   │           ├── Home/Home.jsx
│   │           ├── DealerDetails/DealerDetails.jsx
│   │           └── PostReview/PostReview.jsx
│   ├── manage.py
│   └── requirements.txt
├── .github/workflows/main.yml
└── README.md
```
