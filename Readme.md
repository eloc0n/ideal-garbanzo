# Flask CV App

This is a Flask application that presents CV data via REST API and CLI.

## 🧪 Setting Up a Virtual Environment

## Linux commands
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### Create .env and add these environment variables 
```
export FLASK_APP=app.py
export FLASK_APP=cv_app.core.cli
```

### To run server
```
flask --app core run
```

### To run cli
```
flask --app core.cli cv
```

## Endpoints
### Return full cv
```
http://127.0.0.1:5000/api/cv 
```

### Rest of endpoints
```
http://127.0.0.1:5000/api/contact
http://127.0.0.1:5000/api/skills 
http://127.0.0.1:5000/api/languages
http://127.0.0.1:5000/api/experience
http://127.0.0.1:5000/api/education
http://127.0.0.1:5000/api/interests
```
