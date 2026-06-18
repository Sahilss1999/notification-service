# Mini Notification Service

A backend service for managing notifications with JWT-based user authentication, built using FastAPI and SQLite.

## Features

- User Registration and Login (JWT Authentication)
- Create Notification
- View All Notifications
- View Notification by ID
- Update Notification Status
- Delete Notification
- Search Notifications by Title
- Filter Notifications by Status

## Tech Stack

- **Backend:** Python, FastAPI
- **Database:** SQLite (via SQLAlchemy ORM)
- **Authentication:** JWT (python-jose), Password Hashing (passlib/bcrypt)
- **Frontend:** HTML, CSS, JavaScript

## Project Structure
notification-service/

├── app/

│   ├── auth/            # JWT and password hashing logic

│   ├── models/          # Database models (User, Notification)

│   ├── routes/          # API endpoints

│   ├── schemas/         # Request/response validation

│   ├── database.py      # Database connection setup

│   └── dependencies.py  # Shared dependencies (DB session, auth check)

├── frontend/

│   ├── index.html       # Login/Register page

│   └── dashboard.html   # Notifications dashboard

├── main.py               # App entry point

├── .env                  # Environment variables (not committed)

└── requirements.txt

## Setup Instructions

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd notification-service
```

### 2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root folder:

SECRET_KEY=your-random-secret-key-here
You can generate a secret key using:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### 5. Run the application
```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

### 6. Run the Frontend
Open `frontend/index.html` directly in your browser (or use PyCharm's "Open in Browser" option).

## API Documentation

Interactive API docs are available at: 
http://127.0.0.1:8000/docs


## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Login and receive JWT token |
| POST | `/notifications/` | Create a new notification |
| GET | `/notifications/` | Get all notifications (supports `title` search and `status` filter query params) |
| GET | `/notifications/{id}` | Get a notification by ID |
| PUT | `/notifications/{id}` | Update notification status |
| DELETE | `/notifications/{id}` | Delete a notification |

## Author

Sahil Shetye