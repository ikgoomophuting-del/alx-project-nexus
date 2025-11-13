Project Nexus: E-Commerce Backend (ProDev BE) 

## Introduction
Project Nexus is a real-world e-commerce backend system built as part of the ProDev Backend Engineering program.
It simulates a production-grade development environment emphasizing scalability, security, and performance.

The backend handles:

Product and category management

User authentication and authorization (JWT)

Efficient product filtering, sorting, and pagination

Comprehensive API documentation for easy frontend integration

## Project Goals
CRUD APIs – Build and manage endpoints for products, categories, and users.

Filtering, Sorting & Pagination – Ensure fast, flexible product discovery.

Database Optimization – Apply indexing and schema best practices for performance.

API Documentation – Generate live documentation via Swagger/OpenAPI.

## Technologies Used
Technology	Purpose
Django REST Framework (DRF)	Backend API framework
PostgreSQL	Relational database for product and user data
JWT (JSON Web Tokens)	Secure authentication and session management
drf-yasg / drf-spectacular	API documentation and schema generation
Swagger / Postman	API testing and visualization
Git & GitHub	Version control and collaboration

### Features

## User Authentication
User registration and login via JWT.

Secure endpoints accessible only to authenticated users.

Token-based session management.

## Product & Category Management
Full CRUD (Create, Read, Update, Delete) operations.

Product model includes name, description, price, 7category, and stock quantity. 

Categories can be created and assigned to multiple products.

## Filtering, Sorting & Pagination
Filter products by category:
GET /api/products/?category=electronics

Sort products by price or name:
GET /api/products/?ordering=price or ?ordering=-price

Paginate large datasets:
GET /api/products/?page=2&page_size=10

## API Documentation
Automatically generated Swagger UI at /swagger/ or /api/docs/

Shows all endpoints, request/response examples, and authentication headers.

## Database Optimization
PostgreSQL indexes added on key fields (price, category_id, name) to enhance performance.

Optimized queries using select_related and prefetch_related.

🗂️ Project Structure
ecommerce_backend/
│
├── ecommerce/                # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── products/                 # Product and category app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── users/                    # Authentication app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── requirements.txt
├── README.md
└── manage.py

## Getting Started (Local Setup)
1. Clone the Repository
git clone https://github.com/<your-username>/ecommerce-backend.git
cd ecommerce-backend

2. Create and Activate Virtual Environment
python -m venv venv
source venv/bin/activate      # For Linux/Mac
venv\Scripts\activate         # For Windows

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables
Create a .env file in the project root with:

SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_NAME=ecommerce_db
DATABASE_USER=postgres
DATABASE_PASSWORD=yourpassword
DATABASE_HOST=localhost
DATABASE_PORT=5432

5. Apply Migrations
python manage.py makemigrations
python manage.py migrate

6. Create Superuser
python manage.py createsuperuser

7. Run the Server
python manage.py runserver
Access the project at:
http://127.0.0.1:8000

## API Endpoints Overview
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

## Database Optimization
Indexes created on frequently queried fields:

class Meta:
    indexes = [
        models.Index(fields=['price']),
        models.Index(fields=['name']),
    ]
Efficient queryset usage:

queryset = Product.objects.select_related('category').all()

## API Documentation
Interactive API documentation generated via Swagger:

Swagger UI:
http://127.0.0.1:8000/swagger/

ReDoc:
http://127.0.0.1:8000/redoc/

Includes:

All available endpoints

Request/response models

Example payloads

Authentication details


## Testing the API
Use Postman or cURL to test endpoints:

Example:

curl -X GET http://127.0.0.1:8000/api/products/ \
     -H "Authorization: Bearer <your_jwt_token>"

 ## Author
Ikgopoleng Mophuting
Backend Developer — Project Nexus (ProDev BE)
 [Your Email or GitHub Profile Lin]
