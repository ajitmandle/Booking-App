# Booking System

## Overview
This project is a **Booking System** with a **frontend built using Angular** and a **backend developed using Django with PostgreSQL** as the database.

---

## 📌 Project Structure

```
booking-system/
│-- backend/             # Django Backend
│   │-- manage.py        # Django Management Script
│   │-- settings.py      # Django Configuration
│   │-- .env             # Environment Variables
│-- frontend/            # Angular Frontend
│   │-- src/
│   │-- angular.json     # Angular Configuration
│-- requirements.txt     # Python Dependencies
│-- package.json        # Angular Dependencies
│-- README.md           # Project Documentation
```

---

## 🛠 Backend Setup (Django + PostgreSQL)

### **1️⃣ Prerequisites**
Ensure you have the following installed:
- Python (>=3.8)
- PostgreSQL
- Virtual Environment (`venv`)

### **2️⃣ Installation**
```bash
# Navigate to the backend directory
cd backend

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

# Install dependencies
pip install -r requirements.txt
```

### **3️⃣ Configure Environment Variables**
Create a `.env` file inside the `backend/` directory and add:
```env
DATABASE_URL=postgres://username:password@localhost:5432/booking_db
SECRET_KEY=your_secret_key
DEBUG=True
```

### **4️⃣ Apply Migrations & Run Server**
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Backend will start on **http://127.0.0.1:8000/**

---

## 🌐 Frontend Setup (Angular 17 + Angular Material)

### **1️⃣ Prerequisites**
Ensure you have the following installed:
- Node.js (>=16)
- Angular CLI (>=17)

### **2️⃣ Installation**
```bash
# Navigate to the frontend directory
cd frontend

# Install dependencies
npm install
```

### **3️⃣ Run Development Server**
```bash
ng serve
```
Frontend will start on **http://localhost:4200/**

---

## 📂 Features Implemented
✅ Booking Inventory Display
✅ File Upload Module in Angular
✅ Environment Configuration in Backend
✅ API Integration with Angular Frontend

---

## 🚀 Running Tests

### **Backend Tests (Django + pytest)**
```bash
python manage.py test
```

## 📌 API Endpoints


### **Bookings**
| Method | Endpoint | Description |
|--------|----------|--------------|
| POST | `/api/book/` | Create a new booking |
| POST | `/api/cancel/` | Cancel  booking |
| POST | `/api/upload/` | upload  file |
| GET | `/api/members/` | get  members |
| GET | `/api/inventory/` | get  inventory |
| GET | `/api/bookings/` | get  bookings |
---

## 🛠 Deployment Guide
For deployment, configure `.env` variables and use:
```bash
# Build Angular frontend
cd frontend
ng build --prod

# Deploy Django backend
cd backend
python manage.py collectstatic
```
Use **Docker, AWS, or DigitalOcean** for hosting.

---

## 📝 Contributors
- **[Your Name]** - Ajit Mandale

---

## 📜 License
This project is licensed under [MIT License](LICENSE).

