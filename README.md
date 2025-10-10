🧩 Django CRUD Application

A simple CRUD (Create, Read, Update, Delete) web application built using Django.
This project demonstrates how to manage records (e.g., Students, Employees, Products) using Django’s Model-View-Template (MVT) architecture.

🚀 Features

➕ Create new records via Django Forms

📄 Read and display data in a table

✏️ Update existing records

❌ Delete records

🎨 Clean and responsive UI (with optional Bootstrap or custom CSS)

🗄️ SQLite as the default database

🛠️ Tech Stack

Backend: Django (Python)

Frontend: HTML, CSS (or Bootstrap)

git clone https://github.com/KrishMoond/django
cd django-crud-app

python -m venv env
# Activate on Windows
env\Scripts\activate
# Activate on Mac/Linux
source env/bin/activate

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver



Database: SQLite3 (default Django DB)

Tools: VS Code, Git, Python 3.x
