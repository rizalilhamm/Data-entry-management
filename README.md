# DATA ENTRY MANAGEMENT
This App is Deployed to Heroku and use PostgreSQL as Database Management System

## Installation
First Clone the Repository
```bash
git clone https://github.com/rizalilhamm/flask-crude.git
```

Create Virtual environment
```bash
python -m venv venv
```

Install the Requirements
```bash
pip install -r requirements.txt
```

Create Database in PostgreSQL
```bash
CREATE DATABASE data-entry-management;
```

Create Database Model using Python
```python
from app import app, db
db.create_all()
```

Using Migration
```bash
flask db migrate -m "Initial Migration"
flask db upgdare
```

Note: Create PostgreSQL on Heroku if you want to deploy it and set other Configuration

## Open App
https://flask-crude.herokuapp.com
