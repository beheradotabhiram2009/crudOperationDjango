from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import models

def first(request):
    return HttpResponse("<h1>My first View in django</h1>")

def index(request):
    funda = ['funda','of','web','IT']
    data = "3214"
    return render(request, 'index.html', {'data':data, 'funda':funda})

@csrf_exempt
def student_list(request):
    form = models.Student.objects.all()
    context = {'form':form}
    return render(request, 'students/index.html', context)

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