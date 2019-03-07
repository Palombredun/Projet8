from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect



def login(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return redirect('core:index')
    else:
        pass
    return render(request, 'useres/login.html', {'form': form})