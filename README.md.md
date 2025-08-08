# Book Review Platform API

This project is a Django REST Framework-based API for managing books and reviews.

## Features
- User registration and authentication
- Add, update, delete, and view books
- Add, update, delete, and view reviews for books
- Filter books by author or genre
- View average rating for books

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/book-review-platform.git
cd book-review-platform
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure the database
Edit `settings.py` to update your database configuration. Example for PostgreSQL:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bookreviewdb',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser
```bash
python manage.py createsuperuser
```

### 7. Run the development server
```bash
python manage.py runserver
```

## API Endpoints

### Authentication
- POST `/api/register/` – Register a new user
- POST `/api/token/` – Get JWT token
- POST `/api/token/refresh/` – Refresh JWT token

### Books
- GET `/api/books/` – List all books
- POST `/api/books/` – Create a new book (auth required)
- GET `/api/books/{id}/` – Retrieve a book with average rating
- PUT `/api/books/{id}/` – Update a book (auth required)
- DELETE `/api/books/{id}/` – Delete a book (auth required)

### Reviews
- GET `/api/books/{book_id}/reviews/` – List reviews for a book
- POST `/api/books/{book_id}/reviews/` – Add a review (auth required)
- PUT `/api/books/{book_id}/reviews/{review_id}/` – Update a review (auth required)
- DELETE `/api/books/{book_id}/reviews/{review_id}/` – Delete a review (auth required)

## Running Tests
```bash
python manage.py test
```

## License
This project is licensed under the MIT License.
