New Project Django Project 
1. Project setup (first time)

# 1 Create folder and open it
cd Laptop-brands

# 2 Create virtual environment
python -m venv venv

# 3 Activate virtual environment (Windows)
venv\Scripts\activate

# 4 Install Django
pip install django

# Optional: install bootstrap package for Django templates
pip install django-bootstrap-v5
2. Create Django project and app
# Create project
django-admin startproject Project .

# Create app
python manage.py startapp Mainpage
3. Folder structure (important)
Laptop-brands/
  manage.py
  Project/
    settings.py
    urls.py
  Mainpage/
    views.py
    urls.py
  templates/
    Mainpage.html
templates/ folder banana recommended hai (especially when using render() in views).

4. settings.py changes
File: settings.py

INSTALLED_APPS me app add karo:

INSTALLED_APPS = [
'mainpage'
  'django bootstrap5', # if using bootstrap Package
  ]

  
Templates folder path add karo:
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / 'templates'],
        ...
    },
]
5. views.py
File: views.py

from django.shortcuts import render

def home(request):
    return render(request, 'Mainpage.html')
6. app urls.py create karo
File: urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
7. project urls.py connect karo
File: urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Mainpage.urls')),
]
8. Run project
python manage.py migrate
python manage.py runserver
Open: http://127.0.0.1:8000/

9. GitHub push (quick)
git init
git add .
git commit -m "Initial Django setup"
git branch -M main
git remote add origin https://github.com/Armaan-7814/Laptop-brands-.git
git push -u origin main


*How it works (simple)*

startproject -> main Django config files banata hai.
startapp -> feature/module banata hai (views.py, models.py, etc.).
views.py -> function likhte ho jo page return karta hai.
urls.py -> URL ko view function se connect karta hai.
templates/ -> HTML files rakhte ho.
runserver -> local server start karta hai.

#
