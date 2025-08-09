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

## Project Demo

<img width="1380" height="576" alt="1" src="https://github.com/user-attachments/assets/75fc032f-9bd0-4cc9-b8d4-e1a419e8cb40" />
<img width="1374" height="724" alt="3" src="https://github.com/user-attachments/assets/29f8b4d3-6a0d-45ee-9199-da8ba3adcefb" />
<img width="1385" height="659" alt="4" src="https://github.com/user-attachments/assets/27af3626-6bfe-4992-ae5d-8b5a41bb621c" />
<img width="1400" height="534" alt="5" src="https://github.com/user-attachments/assets/1e5ac432-134c-4e30-bb30-9bb69c2761a8" />
<img width="1379" height="612" alt="6" src="https://github.com/user-attachments/assets/45bb571d-87d5-4480-bdab-9f40042916df" />
<img width="1402" height="660" alt="7" src="https://github.com/user-attachments/assets/2f090f3d-8c04-4e4b-b5ad-3a22b8298312" />
<img width="1381" height="696" alt="8" src="https://github.com/user-attachments/assets/f58f9720-2b4c-474f-960b-bff164ef8c67" />
<img width="1394" height="562" alt="10" src="https://github.com/user-attachments/assets/a354b6fb-5fab-47e6-b9ff-c957f68ce108" />
<img width="1400" height="425" alt="11" src="https://github.com/user-attachments/assets/83b8b942-7b39-451a-ba79-3cc577730d85" />

