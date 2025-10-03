# Django Healthcare Backend

This project is a backend system for a healthcare application built with Django, DRF, PostgreSQL, and JWT authentication.  

## Features
- User registration and login with JWT
- CRUD for Patients and Doctors
- Assign doctors to patients
- Authentication-protected endpoints

## Setup
1. Install dependencies from `requirements.txt`.
2. Configure `.env` with database credentials.
3. Run migrations:
   - python manage.py makemigrations
   - python manage.py migrate
4. Start server:
   - python manage.py runserver

## API Endpoints
- /api/auth/register/
- /api/auth/login/
- /api/patients/
- /api/doctors/
- /api/mappings/
