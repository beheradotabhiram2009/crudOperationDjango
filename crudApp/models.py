from django.db import models

class Student(models.Model):
    rollno = models.CharField(max_length=14, null=False, unique=True, primary_key=True)
    name = models.CharField(max_length=50, null=False)
    branch = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=80, null=True)
    dob = models.DateTimeField(null=True)