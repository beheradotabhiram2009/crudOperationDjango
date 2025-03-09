# crudOperationDjango
### To Check the version of Python installed in your system, run
```
C:\Users\username> python –V
```
### To check pip version, type the following command
```
C:\Users\username> python -m pip –version
```
### Now, use the following command to install Django
```
pip install django
```
### To create a new project crudProject in django
```
C:\Users\username> django-admin startproject crudProject
```
### Change directory to crudProject
```
C:\Users\username> cd crudProject
```
### Change settings.py as given below
```
ALLOWED_HOSTS = ["localhost",  “127.0.0.1:8000”]
```
### To Run the Server
```
python manage.py runserver
```
### To Check the Web page type in browser
```
http://127.0.0.1:8000/
```
### Type the command to create application crudApp
```
python manage.py startapp crudApp
```
### Open the folder crudProject in visual studio code
### Install Python debugger and Sqlite DB explorer
### Write following code in views.py
```
from django.shortcuts import render
from django.http import HttpResponse

def firstView(request):
    return HttpResponse("<h1>My first View in django</h1>")

def indexView(request):
    funda = ['funda','of','web','IT']
    data = "3214"
    return render(request, 'index.html', {'data':data, 'funda':funda})
```
### create a file crudApp/urls.py with the following content:
```
from django.urls import path
from .views import indexView, firstView

urlpatterns = [
    path("", indexView, name="index"), 
    path("first/", firstView),
]
```
### Edit the global crudProject/urls.py as follow:
```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("crudApp/", include("crudApp.urls")),
    path('admin/', admin.site.urls),
]
```
### Edit settings.py as given below
```
from pathlib import Path
import os

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'crudApp\\templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
### Create a folder templates under crudApp directory
### Create a file index.html under template folder and write following html code
```
<html>
<body>
    <h1>This is a HTML page</h1>
    <h1>{{data}}</h1>
    <p>This is a paragraph tag</p>
    
    {% for info in funda %} <!-- info is the variable name-->
        {{info}} <br>
    {% endfor %}
</body>
</html>
```
### To Run the Server type on the terminal
``` python manage.py runserver ```
