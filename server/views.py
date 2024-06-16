from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


def login_view(request): 
    if request.method == 'GET':
      return render(request, "registration/login.html")
    
    elif request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            
            is_professor = request.user.groups.all().filter(name='professor').exists()
            request.session['is_professor'] = is_professor
            
            return redirect('exercises_list')
        else:
            messages.error(request, "Username or Password does not match...")
            
    return render(request, "registration/login.html")
