# Copilot Instructions for AI Coding Agents

## Project Overview
This is a Django-based CRUD application for managing student records. The main components are:
- `crudproject/`: Django project settings and root URLs
- `student/`: Django app containing models, forms, views, URLs, and templates for student management

## Architecture & Data Flow
- **Models**: Defined in `student/models.py` (e.g., `Student` model)
- **Forms**: Custom forms in `student/forms.py` for student data entry and updates
- **Views**: CRUD logic in `student/views.py` using Django's class-based and function-based views
- **Templates**: HTML files in `student/templates/student/` for list and update views
- **URLs**: App-specific routes in `student/urls.py`, included in the project's `crudproject/urls.py`
- **Database**: SQLite (`db.sqlite3`) is used for local development

## Developer Workflows
- **Run Server**: `python manage.py runserver`
- **Apply Migrations**: `python manage.py makemigrations student` then `python manage.py migrate`
- **Create Superuser**: `python manage.py createsuperuser` (for admin access)
- **Run Tests**: `python manage.py test student`

## Project-Specific Patterns
- **Templates**: All student-related templates are under `student/templates/student/`
- **Migrations**: Managed in `student/migrations/`
- **Forms**: Use Django forms for validation and rendering; see `student/forms.py`
- **Views**: CRUD operations are split into separate views (list, update, etc.)
- **Admin**: Student model is registered in `student/admin.py` for Django admin interface

## Integration Points
- No external APIs or services are integrated by default
- All communication is internal via Django ORM and template rendering

## Conventions
- App code lives in `student/`, project config in `crudproject/`
- Use Django's built-in tools for migrations, testing, and admin
- Follow Django's standard directory and naming conventions

## Key Files
- `student/models.py`: Data model definitions
- `student/views.py`: CRUD logic
- `student/forms.py`: Form definitions
- `student/urls.py` & `crudproject/urls.py`: Routing
- `student/templates/student/`: HTML templates

---

**For AI agents:**
- Always use Django management commands for setup and testing
- Reference the above files for examples of CRUD patterns and template usage
- Avoid introducing non-Django patterns unless explicitly requested
- If adding new features, follow the structure and naming conventions shown in the existing `student` app

---

*Please review and suggest any missing or unclear sections for further improvement.*
