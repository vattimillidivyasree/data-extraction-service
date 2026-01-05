# Data Extraction Service API

Backend service built with Django REST Framework.

---

## 📦 Installation & Setup

### 1. Clone the repository
```bash
git clone <YOUR_GITHUB_REPO_URL>
cd data-extraction-service
```

---

### 2. Create virtual environment
```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**Mac / Linux**
```bash
source venv/bin/activate
```

---

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

### 4. Environment variables
Create `.env` file from example:
```bash
cp .env.example .env
```

---

### 5. Run database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Create superuser (optional)
```bash
python manage.py createsuperuser
```

---

### 7. Run development server
```bash
python manage.py runserver
```

Server will start at:
```
http://127.0.0.1:8000/
```

---

## 🔍 API Endpoints

### Health Check
```http
GET /api/v1/health/
```

Response:
```json
{
  "status": "ok"
}
```

---

### Create Extraction Job
```http
POST /api/v1/extractions/
```

---

### Get Extraction Job Status
```http
GET /api/v1/extractions/{job_id}/
```

---

## 📘 API Documentation (Swagger)

Open Swagger UI:
```
http://127.0.0.1:8000/swagger/
```

---

## 🧪 Run Tests
```bash
python manage.py test
```

---

## ✅ Project Status

- ✔ Django server running
- ✔ Database migrations applied
- ✔ Health API working
- ✔ Extraction APIs working
- ✔ Swagger UI enabled

---

## 📤 Submission Instructions

1. Push project to GitHub  
2. Email repository link to:
```
jbirch@glynac.ai
```

**Email Subject**
```
FINAL BACKEND PROJECT
```

3. Notify on Microsoft Teams  
   → GreenTree channel (Springer Capital Teams)

---