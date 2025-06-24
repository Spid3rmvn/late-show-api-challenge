# Late Show API Challenge

A Flask REST API for managing a Late Night TV show system with guests, episodes, and appearances.

## Features

- **MVC Architecture**: Clean separation of concerns
- **PostgreSQL Database**: Robust data storage
- **JWT Authentication**: Secure token-based auth
- **RESTful API**: Standard HTTP methods and status codes
- **Input Validation**: Data integrity and error handling
- **Cascade Deletes**: Automatic cleanup of related data

## Tech Stack

- Flask
- PostgreSQL
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-JWT-Extended
- Werkzeug (password hashing)

## Setup Instructions

### Prerequisites
- Python 3.8+
- PostgreSQL
- Pipenv

### 1. Clone Repository
```bash
git clone https://github.com/<username>/late-show-api-challenge.git
cd late-show-api-challenge
```

### 2. Install Dependencies
```bash
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
pipenv shell
```

### 3. Database Setup
Create PostgreSQL database:
```sql
CREATE DATABASE late_show_db;
```

Update `server/config.py` with your database credentials:
```python
SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/late_show_db'
```

### 4. Initialize Database
```bash
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial migration"
flask db upgrade
```

### 5. Seed Database
```bash
python server/seed.py
```

### 6. Run Application
```bash
python server/app.py
```

The API will be available at `http://localhost:5000`

## Authentication Flow

### 1. Register a New User
```bash
POST /register
Content-Type: application/json

{
    "username": "your_username",
    "password": "your_password"
}
```

### 2. Login to Get JWT Token
```bash
POST /login
Content-Type: application/json

{
    "username": "your_username",
    "password": "your_password"
}
```

Response:
```json
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "user": {
        "id": 1,
        "username": "your_username"
    }
}
```

### 3. Use Token in Protected Routes
```bash
Authorization: Bearer <your_jwt_token>
```

## API Endpoints

| Route | Method | Auth Required? | Description |
|-------|--------|----------------|-------------|
| `/register` | POST | ❌ | Register a user |
| `/login` | POST | ❌ | Log in + return JWT |
| `/episodes` | GET | ❌ | List episodes |
| `/episodes/<int:id>` | GET | ❌ | Get episode + appearances |
| `/episodes/<int:id>` | DELETE | ✅ | Delete episode + appearances |
| `/guests` | GET | ❌ | List guests |
| `/appearances` | POST | ✅ | Create appearance |

## Sample Requests & Responses

### Get All Episodes
```bash
GET /episodes
```

Response:
```json
[
    {
        "id": 1,
        "date": "2024-01-15",
        "number": 1001
    }
]
```

### Get Episode with Appearances
```bash
GET /episodes/1
```

Response:
```json
{
    "id": 1,
    "date": "2024-01-15",
    "number": 1001,
    "appearances": [
        {
            "id": 1,
            "rating": 5,
            "guest_id": 1,
            "episode_id": 1,
            "guest": {
                "id": 1,
                "name": "Jennifer Lawrence",
                "occupation": "Actress"
            }
        }
    ]
}
```

### Create Appearance (Protected)
```bash
POST /appearances
Authorization: Bearer <token>
Content-Type: application/json

{
    "rating": 4,
    "guest_id": 2,
    "episode_id": 1
}
```

## Testing with Postman

1. Import `challenge-4-lateshow.postman_collection.json` into Postman
2. Set the `base_url` variable to `http://localhost:5000`
3. Register a new user or login with existing credentials
4. Copy the JWT token from the login response
5. Set the `jwt_token` variable in Postman
6. Test protected routes with the Authorization header

## Data Models

### User
- `id`: Primary key
- `username`: Unique username
- `password_hash`: Hashed password

### Guest
- `id`: Primary key
- `name`: Guest name
- `occupation`: Guest occupation

### Episode
- `id`: Primary key
- `date`: Episode air date
- `number`: Unique episode number

### Appearance
- `id`: Primary key
- `rating`: Rating (1-5)
- `guest_id`: Foreign key to Guest
- `episode_id`: Foreign key to Episode

## Error Handling

The API returns appropriate HTTP status codes:
- `200`: Success
- `201`: Created
- `400`: Bad Request
- `401`: Unauthorized
- `404`: Not Found
- `500`: Internal Server Error

## GitHub Repository

Repository: https://github.com/<username>/late-show-api-challenge

## Development Notes

- Passwords are hashed using Werkzeug's security functions
- JWT tokens expire after 24 hours
- Episode deletion cascades to related appearances
- Rating validation ensures values are between 1-5
- All endpoints include proper error handling

## Future Enhancements

- Add pagination for large datasets
- Implement role-based access control
- Add more detailed logging
- Include API rate limiting
- Add comprehensive test suite
