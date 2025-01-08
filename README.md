# FastAPI Social Media API

This project is a **RESTful API** built with **FastAPI** for a simple social media application. It supports user authentication, post creation, and a voting system, using **PostgreSQL** as the database and **SQLAlchemy ORM** for database management.

## Features

### API Endpoints
1. **Users**:
   - Create new users.
   - Secure password storage with hashing.
2. **Posts**:
   - Create, read, update, and delete posts.
   - Associate posts with specific users.
3. **Votes**:
   - Users can vote on posts (like functionality).
   - Prevent duplicate votes.
4. **Authentication**:
   - User login with JWT-based authentication.

### Database Models
1. **Users**:
   - Fields: `id`, `email`, `password`, `created_at`.
   - Securely stores user credentials.
2. **Posts**:
   - Fields: `id`, `title`, `content`, `published`, `created_at`, `owner_id`.
   - Linked to a specific user.
3. **Votes**:
   - Composite primary key of `user_id` and `post_id`.
   - Tracks user interactions with posts.

## Technologies Used
- **FastAPI**: High-performance framework for building APIs.
- **SQLAlchemy**: ORM for database modeling and interactions.
- **PostgreSQL**: Relational database for data persistence.
- **JWT**: Authentication and secure token generation.
- **Python**: Programming language used for the backend logic.

## Prerequisites

1. Python 3.7 or higher installed.
2. PostgreSQL database configured.

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/fastapi-social-media-api.git
   cd fastapi-social-media-api
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables for database connection (e.g., `.env` file):
   ```
   DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<database>
   ```

4. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Access the API documentation:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Project Structure
- **`app/models.py`**: SQLAlchemy database models for Users, Posts, and Votes.
- **`app/database.py`**: Database connection setup.
- **`app/main.py`**: Main application file with FastAPI instance and routing.
- **`app/schemas.py`**: Pydantic models for request and response validation.
- **`app/routers`**: Modularized API route handlers for users, posts, and votes.

## Example

### User Creation
**POST** `/users`
```json
{
  "email": "example@example.com",
  "password": "securepassword"
}
```

### Create Post
**POST** `/posts`
```json
{
  "title": "My First Post",
  "content": "This is the content of the post",
  "published": true
}
```

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author
**Prabhu Shankar**  
GitHub: [Your GitHub Profile](https://github.com/yourusername)  
Email: [Your Email]  
