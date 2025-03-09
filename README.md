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
``` 
python manage.py runserver
 ```
### To Check the Web page type in browser
http://127.0.0.1:8000/crudApp/
http://127.0.0.1:8000/crudApp/first
### For Database Operation and administration create a super user by command at terminal
```
python manage.py createsuperuser
```
### To see the django admin site page use in browser
http://127.0.0.1:8000/admin/
### Create a Student model in models.py file
```
from django.db import models

class Student(models.Model):
    rollno = models.CharField(max_length=14, null=False, unique=True, primary_key=True)
    name = models.CharField(max_length=50, null=False)
    branch = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=80, null=True)
    dob = models.DateTimeField(null=True)
```
### Make Change in settings.py to include the crudApp 
```
INSTALLED_APPS = [
    'crudApp.apps.CrudappConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
### Write command for migration which will create database table in sqlite3
```
py manage.py makemigrations
```
### Now we have to register the model for this write in  admin.py following code
```
from django.contrib import admin
from .models import Student

admin.site.register(Student)
```
### Now migrate the table using the following command 
```py manage.py migrate```
### The table created with name crudApp_student
### To add sample data we can install DB Browser for (SQLite) on the system and use it
### or to create a sql file in vscode use command ctrl shift p
### select sqlite: New Query
### select the db.sqlite3 database
### type the insert query
```
insert into crudApp_student (rollno, name, branch, phone, email, dob) values
('101', 'rama', 'cse', '8895955560', 'behera.abhiram2009@gmail.com', '1972-06-14')
```
### To run the Query Type  ctrl shift p
### select sqlite: Run Query
### To check if inserted write SELECT QUERY in sql file and run
```SELECT * from crudApp_student```
### On right side we can see the result
### To show student Data,  write following function in views.py
```
from django.views.decorators.csrf import csrf_exempt
from . import models

@csrf_exempt
def student_list(request):
    form = models.Student.objects.all()
    context = {'form':form}
    return render(request, 'students/index.html', context)
```
### Edit local urls.py as given below
```
urlpatterns = [
    path("", views.index, name="index"), 
    path("first/", views.first),
    path('students/', views.student_list, name="student_list"),
    ]
```
### Create students folder under templates and add index.html file under it
```
<html>
    <head>
        <style>
            .evenrow{ background-color:bisque; }
            .oddrow { background-color: rgb(222, 217, 217); }
        </style>
    </head>
    <body>
    <div align="center">
    <table cellspacing="0" cellpadding="10" border="0">
        <thead><h2 style="color: #1da85b;"><u>Student List</u></h2></thead>
        <thead align="left"><th ><a href="./student_entry" ><input type="button" value="Add Student" /></a></th></thead>
        <thead style="background-color: rgb(92, 67, 139); color: #f7f8f9;">
            <tr>
                <th scope="col">Roll No</th>
                <th scope="col">Name</th>
                <th scope="col">Branch</th>
                <th scope="col">phone</th>
                <th scope="col">email</th>
                <th scope="col">DOB</th>
                <th scope="col">Edit</th>
                <th scope="col">Delete</th>
            </tr>
        </thead>
        {% for info in form %} 
        <tr class="{%cycle "evenrow" "oddrow" %}">
            <td>  {{info.rollno}} </td>
            <td>  {{info.name}}   </td>
            <td>  {{info.branch}} </td>
            <td>  {{info.phone}}  </td>
            <td>  {{info.email}}  </td>
            <td>  {{info.dob|date:'d-M-Y'}}  </td>
            <td><a href="./edit_student/{{info.rollno}}"><input type="button" value="Edit"/></a></td>
            <td><a href="./delete_student/{{info.rollno}}"><input type="button" value="Delete"/></a></td>
        </tr>
        {% endfor %}
    </table>
    </div>
    </body>
</html>
```
### To Run the Server type on the terminal
```
python manage.py runserver
```
### To Check the Web page type in browser
http://127.0.0.1:8000/crudApp/students
### To Add students create student_entry and add_student view
```
@csrf_exempt
def student_entry(request):
    form = []
    context = {'form':form}
    return render(request, 'students/insert_student.html', context)

@csrf_exempt
def add_student(request):
   if request.method == "POST":
      rno = request.POST['rollno']
      nm = request.POST['name']
      br= request.POST['branch']
      ph = request.POST['phone']
      mail = request.POST['email']
      db = request.POST['dob']
      obj = models.Student(rollno=rno, name=nm, branch=br, phone=ph, email=mail, dob=db)
      obj.save()
      return redirect('student_list')
   return HttpResponse("<h2>Unable to add student Record.</h2>")
```
### Under templates/students folder create insert_student.html  file 
```
<html>
<body>
<div align="center">
        <h2 style="color: #1da85b;"><u>Enter Student Data To Insert</u></h2>
        <form action="add_student" method="post">
       <fieldset style="width: 500;">            
          <legend>Insert Student data here</legend>
            <table style="color: #9a1fa5;" cellspacing="5" cellpadding="5">
                <tr>
                    <td><label for="rollno">Roll No: </label></td>
                    <td><input id="rollno" type="text" name="rollno"></td>
                </tr>
                <tr>
                    <td><label for="name">Name: </label></td>
                    <td><input id="name" type="text" name="name"></td>
                </tr>
                <tr>
                    <td><label for="branch">Branch: </label></td>
                    <td><input id="branch" type="text" name="branch"></td>
                </tr>
                <tr>
                    <td><label for="email">Email: </label></td>
                    <td><input id="email" type="text" name="email"></td>
                </tr>
                <tr>
                    <td><label for="phoneno">Phone Number: </label></td>
                    <td><input id="phone" type="text" name="phone"></td>
                </tr>
                <tr>
                    <td><label for="dob">Date of Birth: </label></td>
                    <td><input id="dob" type="date" name="dob"></td>
                </tr>
                <tr align="left">
                    <td></td>
                    <td>
                        <input type="submit" value="Insert">
                        <a href="."><input type="button" value="Cancel"/></a>
                    </td>
                </tr>
            </table>
            </fieldset>
  </form>
</div>
</body>
</html>
```
### Make  change in crudApp/urls.py
```
urlpatterns = [
    path("", views.index, name="index"), 
    path("first/", views.first),
    path('students/', views.student_list, name="student_list"),
    path('students/student_entry', views.student_entry, name="student_entry"),
    path("students/add_student", views.add_student, name='add_student'),
    path('students/edit_student/<rno>', views.edit_student, name="edit_student"),
    path("students/edit_student/update_student/<rno>", views.update_student, name='update_student'),
    path("students/delete_student/<rno>", views.delete_student, name='delete_student'),
    ]
```
### To Run the Server type on the terminal
``` python manage.py runserver ```
### To Check the Web page type in browser
http://127.0.0.1:8000/crudApp/students
### To provide Edit and delete operation  create the views in views.py
```
@csrf_exempt
def edit_student(request, rno):
    thestudent = models.Student.objects.get(rollno=rno)
    context = {'thestudent':thestudent}
    return render(request, 'students/edit_student.html', context)

@csrf_exempt
def delete_student(request, rno):
  thestudent = models.Student.objects.get(rollno=rno)
  thestudent.delete()
  return redirect('student_list')

@csrf_exempt
def update_student(request, rno):
  if request.method == "POST":
      obj = models.Student.objects.get(rollno=rno)
      obj.name = request.POST['name']
      obj.branch= request.POST['branch']
      obj.phone = request.POST['phone']
      obj.email = request.POST['email']
      obj.dob = request.POST['dob']
      obj.save()
      return redirect('student_list')
  return HttpResponse("<h2>Unable to update student Record.</h2>")
```
### Now create template edit.html under templates/students
```
<html>
    <body>
        <h2 style="color: #1da85b;" align="center"><u>Edit Student Data</u></h2>
        <div align="center">
        <form action="update_student/{{thestudent.rollno}}" method="post">
          <fieldset style="width: 500;">
            <legend>Edit Student data here</legend>
            <table style="color: #9a1fa5;" cellspacing="5" cellpadding="5">
                <tr>
                    <td><label for="name">Name: </label></td>
                    <td><input id="name" type="text" name="name" value="{{thestudent.name}}"></td>
                </tr>
                <tr>
                    <td><label for="branch">Branch: </label></td>
                    <td><input id="branch" type="text" name="branch" value="{{thestudent.branch}}"></td>
                </tr>
                <tr>
                    <td><label for="email">Email: </label></td>
                    <td><input id="email" type="text" name="email" value="{{thestudent.email}}"></td>
                </tr>
                <tr>
                    <td><label for="phoneno">Phone Number: </label></td>
                    <td><input id="phone" type="text" name="phone" value="{{thestudent.phone}}"></td>
                </tr>
                <tr>
                    <td><label for="dob">Date of Birth: </label></td>
                    <td><input id="dob" type="date" name="dob" 
                        value="{{thestudent.dob|date:'Y-m-d'}}"></td>
                </tr>
                <tr align="left">
                    <td></td>
                    <td>
                        <input type="submit" value="Update"/>
                        <a href="../"><input type="button" value="Cancel"/></a>
                    </td>
                </tr>
            </table>
            </fieldset>
        </form>
        </div>
        </body>
        </body>
    </body>
</html>
```
### To Run the Server type on the terminal
``` python manage.py runserver ```
### To Check the Web page type in browser
 http://127.0.0.1:8000/crudApp/students 
