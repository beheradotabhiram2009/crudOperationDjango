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
