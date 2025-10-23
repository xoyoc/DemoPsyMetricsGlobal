# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

PsyMetrics Global is a Django 5.2 web application for online psychometric assessments with Tailwind CSS. The application provides NOM-035 evaluations and a consultation platform with psychologists.

## Key Commands

### Development Environment Setup
```bash
# Create and activate virtual environment (recommended: .venv_psmetrics)
python -m venv .venv_psmetrics
source .venv_psmetrics/bin/activate

# Install dependencies
pip install -r requirements.txt

# Setup database and create superuser
python manage.py migrate
python manage.py createsuperuser

# Build Tailwind CSS (required before running server)
python manage.py tailwind build
```

### Running the Development Server
```bash
# Standard development server
python manage.py runserver

# With Tailwind live reload (uses honcho and Procfile.tailwind)
honcho start -f Procfile.tailwind
```

### Database Operations
```bash
# Create migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Reset database (SQLite in development)
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Static Files and Assets
```bash
# Build Tailwind CSS for production
python manage.py tailwind build

# Collect static files (for deployment)
python manage.py collectstatic --noinput
```

### Testing and Validation
```bash
# Check for deployment issues (production settings)
python manage.py check --deploy

# Django shell for manual testing/debugging
python manage.py shell
```

### Deployment
```bash
# Run deployment script (migrations, static files, Tailwind build)
./deploy.sh

# Production server with Gunicorn
gunicorn psymetrics.wsgi:application --config gunicorn.conf.py
```

## Architecture

### Application Structure

**Core Applications:**
- `psymetrics/` - Main Django project configuration with settings for development and production
- `evaluaciones/` - Handles NOM-035 psychometric evaluations and custom assessments
- `consultas/` - Manages psychological consultations and psychologist availability
- `theme/` - Tailwind CSS configuration and static assets

### Data Models Overview

**Evaluaciones App:**
- `CuestionarioNOM035` - Questionnaire definitions with versions and states (draft/active/inactive)
- `DominioNOM035` - Questionnaire domains/sections with ordering
- `PreguntaNOM035` - Individual questions (Likert scale, multiple choice, open-ended)
- `OpcionRespuesta` - Answer options linked to questions with scoring values
- `Evaluacion` - Assessment instances tracking evaluator, evaluated user, and completion state
- `RespuestaEvaluacion` - Individual responses with scores and timestamps
- `TipoEvaluacion` & `EvaluacionPersonalizada` - Custom evaluation types with pricing

**Consultas App:**
- `Psicologo` - Psychologist profiles with specialties (organizational, clinical, cognitive, industrial, social)
- `TipoConsulta` - Consultation types with duration and pricing
- `Consulta` - Consultation sessions with state tracking (requested → confirmed → in progress → completed/cancelled)
- `DisponibilidadPsicologo` - Psychologist availability schedule by day/time
- `MensajeConsulta` - In-consultation messaging system

### Settings Configuration

The project uses two settings files:
- `psymetrics/settings.py` - Development settings (SQLite, DEBUG=True, django-browser-reload)
- `psymetrics/settings_production.py` - Production settings (PostgreSQL, security headers, logging, Redis cache)

Production uses environment variables for:
- Database credentials (DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)
- ALLOWED_HOSTS, SECRET_KEY
- Email configuration (EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
- REDIS_URL for caching

### URL Routing

Main URL structure:
- `/` - Evaluaciones app (home, services, about, contact, dashboard)
- `/consultas/` - Consultas app (consultation listing and booking)
- `/admin/` - Django admin interface

## Technology Stack

- **Framework:** Django 5.2 with Python 3.12+
- **Styling:** Tailwind CSS 4.2 via django-tailwind
- **Database:** SQLite (development), PostgreSQL (production)
- **Authentication:** Django built-in auth system
- **Development:** django-browser-reload for hot reload
- **Production Server:** Gunicorn with custom configuration
- **Deployment:** DigitalOcean App Platform (see .do/app.yaml)

## Important Notes

### Tailwind CSS Integration
The Tailwind CSS must be compiled before running the app. The project uses django-tailwind with a dedicated `theme` app. For development, run `honcho start -f Procfile.tailwind` to enable live CSS rebuilding.

### Static Files
Static files are configured differently for dev and production:
- Development: Served by Django from `theme/static_src/`
- Production: Collected to `staticfiles/` via `collectstatic`, served by Nginx/CDN

### Database Migrations
All model changes must be reflected in migrations. The project has two apps with separate migrations directories. Always run `makemigrations` for both apps after model changes.

### Security Configuration
Production settings enforce:
- HTTPS-only cookies (SESSION_COOKIE_SECURE, CSRF_COOKIE_SECURE)
- XSS and content type sniffing protection
- X-Frame-Options set to DENY
- Comprehensive logging to files and console

### Localization
The application is configured for Spanish (es-es) in Mexico City timezone (America/Mexico_City).

### Virtual Environment
The project recommends using `.venv_psmetrics` as the virtual environment name (already exists in the repository).

## Deployment Considerations

**DigitalOcean App Platform:**
- Configuration in `.do/app.yaml`
- Uses Gunicorn on port 8000
- Requires PostgreSQL database setup
- Environment variables must be configured in DO control panel

**Pre-deployment Checklist:**
1. Update SECRET_KEY and set DEBUG=False
2. Configure ALLOWED_HOSTS with production domains
3. Set up PostgreSQL database and DATABASE_URL
4. Run `python manage.py tailwind build`
5. Run `python manage.py collectstatic`
6. Apply migrations with `python manage.py migrate`
7. Configure CSRF_TRUSTED_ORIGINS for production domain
