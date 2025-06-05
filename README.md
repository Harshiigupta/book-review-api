Book Review API (Python + SQLite)

This is a simple RESTful API built using Python, Flask, and SQLite for a Book Review system.
🚀 Features

    User Signup/Login using JWT Authentication

    Add/Get Books (with pagination and filtering)

    Add/Update/Delete Book Reviews (1 review per user per book)

    Search books by title or author (case-insensitive)

    Simple SQLite database (no setup needed)

🧰 Tech Stack

    Python 3

    Flask

    SQLite

    JWT (via PyJWT)

    Flask-SQLAlchemy

🗂️ Project Structure

book_review_api/
│
├── app/
│   ├── __init__.py         # Flask app and DB setup
│   ├── models.py           # DB models (User, Book, Review)
│   ├── auth.py             # Signup & Login routes
│   ├── books.py            # Book routes
│   ├── reviews.py          # Review routes
│
├── run.py                  # Entry point to run server
├── requirements.txt        # Dependencies
├── README.md               # Project docs
├── .env                    # Environment variables

⚙️ Setup Instructions

    Clone the repo or unzip the project

    Install dependencies

pip install -r requirements.txt

Set environment variables
Create a .env file:

SECRET_KEY=your_secret_key_here(given in .env file )

Run the server

    python run.py

    Server will run at: http://127.0.0.1:5000

🔐 JWT Authentication

After login, copy the token from the response:

{
  "token": "eyJ0eXAiOiJKV1QiLCJh..."
}

Then send it in request headers like:

Authorization: Bearer YOUR_TOKEN_HERE

🧪 Example API Requests (via Postman)
Signup:

POST /signup

{
  "username": "harshita",
  "password": "mypassword"
}

Login:

POST /login

{
  "username": "harshita",
  "password": "mypassword"
}

Add Book:

POST /books
Headers:

Authorization: Bearer YOUR_TOKEN_HERE

Body:

{
  "title": "The Alchemist",
  "author": "Paulo Coelho",
  "genre": "Fiction"
}

📦 Postman Collection

Use the provided .postman_collection.json file to test the full API easily.
🗃️ Database Schema

    User: id, username, password

    Book: id, title, author, genre

    Review: id, book_id, user_id, rating, comment

✅ Design Notes

    Passwords are hashed using werkzeug.security

    JWT tokens are required for all protected endpoints

    Each user can only review a book once

    Review pagination is supported for scalability

