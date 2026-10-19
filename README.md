# Employee Management Web App

CRUD web app built with Python (Flask), HTML/CSS and SQL Server.

## Features
- Add, view, edit and delete employees
- Search by name or department
- Duplicate email protection (UNIQUE constraint)
- Parameterized SQL queries to prevent SQL injection

## Setup
1. Run create_employee_db.sql in SSMS
2. py -3.12 -m venv venv
3. .\venv\Scripts\Activate.ps1
4. pip install -r requirements.txt
5. Set SERVER in db.py to your SQL Server name
6. python app.py, then open http://127.0.0.1:5000