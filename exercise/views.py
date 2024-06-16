from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
import uuid
from django.contrib.auth.models import User

from student.models import Student
from .models import Exercise, HomeWork
from .forms import ExerciseForm
from utils.decorators.user_is_professor import user_is_professor


@login_required
def exercises_list(request):
  if request.method == 'GET':
    
    groups = request.user.groups.all().filter(name='professor').exists()
    
    print('GROUPS: ', groups)
    
    exercises = Exercise.objects.all()
    return render(request, 'exercises-list.html', { 'exercises': exercises })
  else:
    return Http404()
  
  
@login_required
@user_is_professor
def register_exercise(request):
  if request.method == 'GET':
    return render(request, 'register-exercise.html', { 'form': ExerciseForm })
  
  elif request.method == 'POST':
    form = ExerciseForm(request.POST, request.FILES)
    
    if form.is_valid():
      form.save()
      return redirect('exercises_list')
    else:
      return Http404()
    
  else:
    return Http404()
  
  
@login_required
def exercise_detail(request, id):
  exercise = get_object_or_404(Exercise, pk=id)
  return render(request, 'exercise.html', { 'exercise': exercise })


@login_required
def register_homework(request):
  if request.method == 'POST':
    exercise = Exercise.objects.get(pk=request.POST['exercise'])    
    student = Student.objects.get(pk=request.user.id)
    homework = HomeWork.objects.create(student=student, exercise=exercise)
    homework.code.save(str(uuid.uuid4()) + '.py', request.FILES['file'])
    
    return redirect('exercises_list')
    
  else:
    return Http404()
  
  
@login_required
@user_is_professor
def delete_exercise(request, id):
   exercise = get_object_or_404(Exercise, pk=id)
   exercise.delete()
   
   return redirect('exercises_list')