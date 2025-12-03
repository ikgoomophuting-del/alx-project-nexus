Project Nexus: E-Commerce Backend (ProDev BE)
Introduction

Project Nexus is a production-grade e-commerce backend built as part of the ProDev Backend Engineering program.
It simulates a real-world environment emphasizing scalability, security, and performance.

The backend provides:

Product, category, and review management

User authentication and authorization (JWT)

Product filtering, sorting, and pagination

Live API documentation via Swagger / ReDoc

Project Goals

CRUD APIs – Build endpoints for products, categories, and reviews.

Filtering, Sorting & Pagination – Allow fast product discovery.

Database Optimization – Apply indexing and query optimizations for performance.

API Documentation – Generate Swagger/OpenAPI docs for frontend integration.

Technologies Used
Technology	Purpose
Django REST Framework (DRF)	Backend API framework
PostgreSQL	Relational database for products, categories, users
JWT (JSON Web Tokens)	Authentication and session management
drf-yasg / drf-spectacular	API documentation and schema generation
Swagger / Postman	API testing and visualization
Git & GitHub	Version control and collaboration

Features 
User Authentication

User registration and login with JWT.

Secure endpoints accessible only to authenticated users.

Token-based session management.

Product, Category & Review Management

Products: CRUD operations with fields for name, description, price, category, stock, and owner.

Categories: CRUD operations; can be assigned to multiple products.

Reviews: Users can create, update, and delete reviews for products. Reviews are associated with both the product and the reviewer.

Filtering, Sorting & Pagination

Filter products by category:

GET /api/products/?category=electronics


Sort products by price or name:

GET /api/products/?ordering=price
GET /api/products/?ordering=-price


Paginate large datasets:

GET /api/products/?page=2&page_size=10

API Documentation

Swagger UI: /swagger/

ReDoc: /redoc/

Documentation shows all endpoints, request/response examples, and authentication headers.

Project Structure
ecommerce_backend/
│
├── ecommerce/               # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── products/                # Products, categories, reviews
│   ├── models/              # Product, Category, Review models
│   │   ├── product.py
│   │   ├── category.py
│   │   └── review.py
│   ├── serializers/         # DRF serializers
│   │   ├── product_serializers.py
│   │   └── review_serializer.py
│   ├── views/               # DRF viewsets
│   │   ├── product_views.py
│   │   ├── category_views.py
│   │   └── review_views.py
│   ├── urls.py              # Router-based URLs
│   └── filters/             # DRF filters for products
│       └── product_filters.py
│
├── users/                   # Authentication app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── requirements.txt
├── README.md
└── manage.py

Getting Started (Local Setup)

Clone the Repository

git clone https://github.com/ikgoomophuting-del/ecommerce-backend.git
cd ecommerce-backend


Create and Activate Virtual Environment

python -m venv venv
venv\Scripts\activate         # Windows


Install Dependencies

pip install -r requirements.txt


Configure Environment Variables
Create .env in the project root:

SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_NAME=ecommerce_db
DATABASE_USER=postgres
DATABASE_PASSWORD=yourpassword
DATABASE_HOST=localhost
DATABASE_PORT=5432


Apply Migrations

python manage.py makemigrations
python manage.py migrate


Create Superuser

python manage.py createsuperuser


Run the Server

python manage.py runserver


Access the project at http://127.0.0.1:8000.

API Endpoints Overview
Authentication
Method	Endpoint	Description
POST	/api/auth/register/	Register new user
POST	/api/auth/login/	Obtain JWT access token
POST	/api/auth/logout/	Logout user (optional)

Products
Method	Endpoint	Description
GET	/api/products/	List all products (supports filtering, sorting, pagination)
POST	/api/products/	Create a new product
GET	/api/products/{id}/	Retrieve a specific product
PUT	/api/products/{id}/	Update a product
DELETE	/api/products/{id}/	Delete a product

Categories
Method	Endpoint	Description
GET	/api/categories/	List all categories
POST	/api/categories/	Create a category
PUT	/api/categories/{id}/	Update a category
DELETE	/api/categories/{id}/	Delete a category

Reviews
Method	Endpoint	Description
GET	/api/reviews/	List all reviews
POST	/api/reviews/	Create a review
GET	/api/reviews/{id}/	Retrieve a specific review
PUT	/api/reviews/{id}/	Update a review
DELETE	/api/reviews/{id}/	Delete a review
Database Optimization

Indexes on frequently queried fields: price, category_id, name.

class Meta:
    indexes = [
        models.Index(fields=['price']),
        models.Index(fields=['name']),
    ]


Optimized queries using select_related and prefetch_related for products and reviews.

Testing the API

Use Postman or cURL to test endpoints:

curl -X GET http://127.0.0.1:8000/api/products/ \
     -H "Authorization: Bearer <your_jwt_token>"

Author

Ikgopoleng Mophuting
Backend Developer — Project Nexus (ProDev BE - E-Commerce Backend)
GitHub  https://github.com/ikgoomophuting-del/alx-project-nexus/tree/main
