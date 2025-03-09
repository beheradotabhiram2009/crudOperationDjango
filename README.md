# crudOperationDjango
## To Check the version of Python installed in your system, run
C:\Users\username> python –V
## To check pip version, type the following command
C:\Users\username> python -m pip –version
## Now, use the following command to install Django
pip install django
## To create a new project crudProject in django
C:\Users\username> django-admin startproject crudProject
## Change directory to crudProject
C:\Users\username> cd crudProject
## Change settings.py as given below
ALLOWED_HOSTS = ["localhost",  “127.0.0.1:8000”]
## To Run the Server
python manage.py runserver
## To Check the Web page type in browser
 http://127.0.0.1:8000/
## Type the command to create application crudApp
python manage.py startapp crudApp
