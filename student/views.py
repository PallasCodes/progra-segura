from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .forms import StudentForm, UserForm
from .models import Student
from utils.decorators.user_is_professor import user_is_professor


@login_required
def register_student(request):
  if request.method == 'GET':
    return render(request, 'register-student.html', { 'student_form': StudentForm, 'user_form': UserForm })
  
  elif request.method == 'POST':
    user_form = UserForm(request.POST)
    user = user_form.save()
    
    Student.objects.create(user=user, registration_number=request.POST['registration_number'], full_name=request.POST['full_name'])
    
    return redirect('register_student')
  
  else:
    return Http404()


@login_required
@user_is_professor
def students_list(request):
  if request.method == 'GET':
    students = Student.objects.all()
    return render(request, 'students-list.html', { 'students': students })
  
  else:
    return Http404()