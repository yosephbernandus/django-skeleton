# Django Skeleton

A ready Django project template that serves as the foundation for the [Django Project Generator](https://github.com/yosephbernandus/django-project-generator). This skeleton provides a comprehensive, modern Django setup with best practices, security configurations, and development tools pre-configured.

## Features

- 🚀 **Production-ready features** including caching, logging, and background tasks
- 🔧 **UV Package Manager** - Fast, modern Python package management
- 🌍 **Environment Configuration** - Full `.env` support with `django-environ`
- 📝 **Comprehensive Logging** - Structured logging for requests and application
- 🛠️ **Development Tools** - Ruff, MyPy, pre-commit hooks configure
- 🎨 **Frontend integration** with static files and templatesd
- 🔒 **Security-first approach** - Secure defaults and CORS configuration

## Requirements

- **uv** - [Install uv](https://docs.astral.sh/uv/getting-started/installation/)
- **git** - Version control
- **Python 3.8+** - Will be managed by uv

## Quick Start

```bash
cd my-awesome-project
source .venv/bin/activate
uv run python src/manage.py migrate
uv run python src/manage.py runserver
```

## Project Structure

```
my-project/
├── .env                          # Environment variables
├── .env.example                  # Environment template
├── pyproject.toml               # Project configuration
├── uv.lock                      # Dependency lock file
├── logs/                        # Application logs
│   ├── requests.log            # HTTP requests
│   └── app.log                 # Application logs
└── src/                        # Django source code
    ├── manage.py               # Django management script
    ├── config/                 # Project configuration
    │   ├── settings.py         # Django settings
    │   ├── settings_celery.py  # Celery configuration
    │   ├── urls.py             # URL routing
    │   ├── wsgi.py             # WSGI application
    │   └── asgi.py             # ASGI application
    ├── core/                   # Core utilities
    │   ├── exceptions.py
    │   ├── utils.py
    │   └── validators.py
    ├── users/                  # Example Django app module
    │   ├── models.py
    │   ├── views.py
    │   ├── urls.py
    │   ├── admin.py
    │   └── tests.py
    ├── static/                 # Static files (source)
    │   ├── css/
    │   └── js/
    ├── templates/              # HTML templates
    │   └── users/
    └── staticfiles/           # Collected static files (auto-generated)
```

## Configuration

### Environment Variables

The project uses environment variables for configuration. Key variables include:

```bash
# Core Django Settings
SECRET_KEY="your-secret-key"
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
TIME_ZONE=Asia/Jakarta

# Database Configuration
DB_NAME=myproject_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

# Static Files
STATIC_URL=/static/
STATIC_ROOT=staticfiles

# Redis Configuration
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=1
REDIS_PASSWORD=

# Celery Configuration
BROKER_URL=redis://localhost:6379/0

# Logging
LOG_PATH=logs
ENVIRONMENT=development
```

## Development

### Available Commands

```bash
# Install dependencies
uv sync

# Run development server
uv run python src/manage.py runserver

# Run migrations
uv run python src/manage.py migrate

# Create migrations
uv run python src/manage.py makemigrations

# Collect static files
uv run python src/manage.py collectstatic

# Run tests
uv run python src/manage.py test

# Create superuser
uv run python src/manage.py createsuperuser

# Django shell
uv run python src/manage.py shell_plus
```

### Code Quality Tools

```bash
# Format code with Ruff
uv run ruff format .

# Lint code with Ruff
uv run ruff check .

# Type checking with MyPy
uv run mypy . or ./run-mypy

# Run all quality checks
uv run ruff check . && uv run ruff format . && uv run mypy .
```

### Setup

1. **Environment Variables**
   ```bash
   DEBUG=False
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   SECRET_KEY=your-production-secret
   ```
2. **Static Files**
   ```bash
   uv run python src/manage.py collectstatic --no-input
   ```

3. **Run Migrations**
   ```bash
   uv run python src/manage.py migrate
   ```

4. **Run Django with the datadog**
   ```bash
   uv run ddtrace-run src/manage.py runserver
   ```

### Pre-Commit Hooks
```
# Pre Commit install
pre-commit install

# Run Format And Lint check and fix
pre-commit run ruff

# Run checking type with mypy
pre-commit run mypy
```

## Features

### API Features
- **Django REST Framework** - Full API support
- **CORS Headers** - Cross-origin request handling
- **Health Check Endpoint** - `/api/health/`
- **Interactive API Documentation** - Available in development swagger integration `api/docs/`

### Development Tools
- **Django Extensions** - Enhanced management commands
- **Debug Toolbar** - Development debugging (when enabled)

### Background Tasks
- **Celery** - `celery -A src.config.settings_celery worker -l info -Q default`

