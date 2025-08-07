# MSCHF - FastAPI + PostgreSQL Application

A FastAPI application with PostgreSQL database integration, featuring user management functionality and database migrations with Alembic.

## Features

- FastAPI web framework
- PostgreSQL database with SQLAlchemy ORM
- Database migrations with Alembic
- Docker containerization
- User management API endpoints

## Prerequisites

- Python 3.11+
- Docker and Docker Compose (for containerized setup)
- PostgreSQL (for local development)

## Step-by-Step Setup Guide

### Option 1: Docker Setup (Recommended - Easiest)

**Step 1: Clone the repository**
```bash
git clone <repository-url>
cd mschf
```

**Step 2: Create a virtual environment**
```bash
# On Windows
py -m venv venv
venv\Scripts\activate

# On macOS/Linux
python -m venv venv
source venv/bin/activate

# Verify virtual environment is activated
# You should see (venv) at the beginning of your command prompt
```

**Step 3: Install Python dependencies**
```bash
# Make sure your virtual environment is activated (you should see (venv) in your terminal)
# Then install dependencies using py -m pip (recommended)
py -m pip install -r requirements.txt

# Alternative: using pip directly
pip install -r requirements.txt
```

**Step 4: Check Docker installation**
```bash
# Check if Docker is installed
docker --version

# Check if Docker Compose is installed
docker-compose --version

# If not installed, download from: https://docs.docker.com/get-docker/
```

**Step 5: Create environment file**
Create a file named `.env` in the root directory and add these lines:
```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=pass
POSTGRES_DB=mschf
DATABASE_URL=postgresql://postgres:pass@postgres-db:5432/mschf
```

**Step 6: Build and run with Docker Compose**

```bash
docker-compose up --build
```

**Step 7: Wait for services to start**
- Wait until you see "Application startup complete" in the logs
- This may take 1-2 minutes on first run

**Step 8: Access the application**
- Open your web browser and go to: http://localhost:8000
- For API documentation: http://localhost:8000/docs
- For alternative docs: http://localhost:8000/redoc

**Step 9: Test the API**
- Visit http://localhost:8000/ to see the health check
- Use the interactive docs at http://localhost:8000/docs to test endpoints

## Database Management

### Working with Migrations

The project uses Alembic for database migrations. Here are the common commands:

**Step 1: Create a new migration**
```bash
alembic revision --autogenerate -m "description of changes"
```

**Step 2: Apply migrations**
```bash
alembic upgrade head
```

**Step 3: Rollback migration**
```bash
alembic downgrade -1
```

**Step 4: View migration history**
```bash
alembic history
```

**Step 5: Check current migration status**
```bash
alembic current
```

## Project Structure

```
mschf/
├── alembic/                 # Database migration files
├── app/                     # Main application code
│   ├── __init__.py
│   ├── database.py         # Database configuration
│   ├── dependencies.py     # FastAPI dependencies
│   ├── main.py            # FastAPI application
│   └── models.py          # SQLAlchemy models
├── docker-compose.yml      # Docker Compose configuration
├── Dockerfile             # Docker image definition
├── requirements.txt       # Python dependencies
├── alembic.ini           # Alembic configuration
└── README.md             # This file
```