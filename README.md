# Address Book API

A minimal **Address Book REST API** built using **FastAPI**.
The API allows users to **create, update, delete, and retrieve addresses**, and also find addresses **within a specified distance of given geographic coordinates**.

The application demonstrates best practices in backend development including:

* Clean project architecture
* Input validation using Pydantic
* Database interaction using SQLAlchemy ORM
* Structured logging
* Automated formatting using pre-commit hooks
* Unit testing using pytest
* Environment-based configuration

---

# Tech Stack

* Python 3.12
* FastAPI
* SQLAlchemy ORM
* SQLite
* Pydantic
* Geopy
* Pytest
* Pre-commit (Black, isort, flake8)
* Docker (optional)

---

# Project Structure

```
address-book-api
│
├── app
│   ├── main.py
│
│   ├── core
│   │   ├── config.py
│   │   └── logger.py
│
│   ├── db
│   │   ├── base.py
│   │   └── session.py
│
│   ├── models
│   │   └── address.py
│
│   ├── schemas
│   │   └── address.py
│
│   ├── services
│   │   └── address_service.py
│
│   └── routes
│       └── address.py
│
├── tests
│   ├── conftest.py
│   └── test_address.py
│
├── requirements.txt
├── .env
├── .gitignore
├── .pre-commit-config.yaml
├── Dockerfile
└── README.md
```

The project is structured using **separation of concerns**:

* `routes` → API endpoints
* `services` → business logic
* `models` → database models
* `schemas` → request/response validation
* `db` → database configuration
* `core` → configuration and logging

---

# Features

* Create Address
* Update Address
* Delete Address
* Retrieve Address by ID
* Retrieve All Addresses
* Find Addresses within a given distance
* Input validation for coordinates
* Structured logging
* Unit tests
* Pre-commit code formatting

---

# Address Model

Each address contains:

| Field      | Description            |
| ---------- | ---------------------- |
| id         | Unique identifier      |
| street     | Street name            |
| city       | City                   |
| country    | Country                |
| latitude   | Latitude coordinate    |
| longitude  | Longitude coordinate   |
| created_at | Timestamp when created |
| updated_at | Timestamp when updated |

Coordinates are validated:

* Latitude: -90 to 90
* Longitude: -180 to 180

---

# Running the Application

## 1. Clone the repository

```
git clone <repository-url>
cd address-book-api
```

## 2. Create a virtual environment

```
python -m venv venv
source venv/bin/activate
```

Windows:

```
venv\Scripts\activate
```

## 3. Install dependencies

```
pip install -r requirements.txt
```

## 4. Run the API

```
uvicorn app.main:app --reload
```

The API will start at:

```
http://127.0.0.1:8000
```

---

# API Documentation

FastAPI automatically generates Swagger documentation.

Open in browser:

```
http://127.0.0.1:8000/docs
```

Interactive API testing is available directly from Swagger.

---

# API Endpoints

### Create Address

POST /api/v1/addresses

Example request:

```
{
  "street": "Anna Salai",
  "city": "Chennai",
  "country": "India",
  "latitude": 13.0827,
  "longitude": 80.2707
}
```

---

### Get All Addresses

GET /api/v1/addresses

---

### Get Address by ID

GET /api/v1/addresses/{id}

---

### Update Address

PUT /api/v1/addresses/{id}

Example:

```
{
  "street": "New Street Name"
}
```

Supports partial updates.

---

### Delete Address

DELETE /api/v1/addresses/{id}

---

### Find Nearby Addresses

GET /api/v1/addresses/nearby

Query Parameters:

| Parameter   | Description   |
| ----------- | ------------- |
| lat         | latitude      |
| lon         | longitude     |
| distance_km | search radius |

Example:

```
GET /api/v1/addresses/nearby?lat=13.0827&lon=80.2707&distance_km=5
```

This endpoint uses the **geopy library** to calculate geodesic distance between coordinates.

---

# Running Tests

Run all tests:

```
pytest
```

Expected output:

```
6 passed
```

Tests cover:

* Address creation
* Retrieval
* Update
* Deletion
* Nearby search
* Validation errors

---

# Pre-commit Formatting

This project uses **pre-commit hooks** to enforce code quality.

Tools included:

* Black (code formatting)
* isort (import sorting)
* flake8 (linting)

## Install hooks

```
pre-commit install
```

Run manually:

```
pre-commit run --all-files
```

These checks will automatically run before every commit.

---

# Docker (Optional)

Build image:

```
docker build -t address-book-api .
```

Run container:

```
docker run -p 8000:8000 address-book-api
```

---

# Logging

Application logging is configured in:

```
app/core/logger.py
```

Logs include:

* API requests
* Address creation
* Address updates
* Address deletions
* Error events

---

# Environment Configuration

Configuration values are loaded from:

```
.env
```

Example:

```
DATABASE_URL=sqlite:///./addresses.db
LOG_LEVEL=INFO
API_VERSION=/api/v1
```

---

# Code Quality Practices

This project follows best practices:

* Type hints used throughout
* Validation at request boundaries
* ORM for database access
* Structured logging
* Modular architecture
* Clean dependency management
* Automated formatting

---

# Future Improvements

Potential improvements include:

* Pagination for address listing
* Spatial indexing for faster nearby queries
* PostGIS support for large datasets
* Authentication and authorization
* Integration tests with a dedicated test database

---

# Author

Manikandan R

Software Engineer