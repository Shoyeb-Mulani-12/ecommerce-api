# Ecommerce API Backend

A professional Ecommerce REST API backend built using Django and Django REST Framework (DRF).
This project includes authentication, product management, cart functionality, and order management with a scalable backend architecture.

---

# Features

* JWT Authentication
* Product Management API
* Category Management
* Cart System
* Order Management
* Admin Dashboard
* RESTful APIs
* CRUD Operations
* Relational Database Models
* Permissions & Protected Routes

---

# Tech Stack

* Python
* Django
* Django REST Framework
* Simple JWT
* SQLite
* GitHub

---

# API Endpoints

## Authentication

* `/api/token/`
* `/api/token/refresh/`

## Products

* `/api/products/`

## Categories

* `/admin/`

## Cart

* `/api/carts/`

## Orders

* `/api/orders/`

---

# Installation

```bash
git clone https://github.com/YOUR_USERNAME/ecommerce-api.git

cd ecommerce-api

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

---

# Project Structure

```bash
ecommerce_api/
│
├── core/
├── store/
├── manage.py
├── requirements.txt
└── README.md
```

---

# Authentication

This project uses JWT Authentication.

Generate token:

```bash
POST /api/token/
```

Use access token in headers:

```bash
Authorization: Bearer your_access_token
```

---

# Admin Panel

```bash
http://127.0.0.1:8000/admin/
```

---

# Future Improvements

* Payment Gateway Integration
* Product Image Upload
* PostgreSQL Integration
* Docker Deployment
* Redis Caching
* Swagger API Documentation
* Email Notifications

---

# Author

Shoyeb Mulani

MCA Graduate | Python Backend Developer | AI/ML Enthusiast
