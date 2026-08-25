# Student CRUD Management System

Stack:
- Python
- Django
- MySQL
- HTML
- CSS

## Setup on Windows PowerShell

1. Open this folder in VS Code.
2. Create and activate a virtual environment:

```powershell
python -m venv crudenv
.\crudenv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Create a MySQL database:

```sql
CREATE DATABASE student_crud_db;
```

5. Open `student_crud/settings.py` and change the MySQL USER/PASSWORD if needed.

6. Run migrations:

```powershell
python manage.py makemigrations
python manage.py migrate
```

7. Start the server:

```powershell
python manage.py runserver
```

8. Open http://127.0.0.1:8000/

## Features

- Create student
- Read/view students
- Update student
- Delete student
- Search students
- Responsive HTML/CSS interface
