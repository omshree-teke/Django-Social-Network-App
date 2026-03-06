# Django Social Network App

A full-featured social media web app built with Django — includes real-time chat, video calls, friend system, blog posts, and notifications.

## Features

- 📝 Blog posts with rich text editor (CKEditor 5)
- 💬 Real-time chat using Django Channels & WebSockets
- 📹 Video calls using Agora
- 👥 Friend request system
- 🔔 Notifications
- 🔐 Authentication with email & social login (Google, GitHub)
- 👤 User profiles with avatar
- 📱 Responsive design with Bootstrap 4

## Tech Stack

- **Backend:** Django 4.2
- **Frontend:** Bootstrap 4, JavaScript
- **Real-time:** Django Channels, Daphne, WebSockets
- **Database:** SQLite (dev) / PostgreSQL (prod)
- **Auth:** Django Allauth
- **Editor:** CKEditor 5
- **Video:** Agora RTC
- **Static files:** Whitenoise

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/omshree-teke/Django-Social-Network-App.git
cd Django-Social-Network-App
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create `.env` file in root directory
```
SECRET_KEY=your_secret_key
DEBUG=True
EMAIL_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_email_password
GOOGLE_RECAPTCHA_SECRET_KEY=your_recaptcha_key
```

### 5. Run migrations
```bash
python manage.py migrate
```

### 6. Create superuser
```bash
python manage.py createsuperuser
```

### 7. Run the server
```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000**
