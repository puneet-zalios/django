from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/reporting/')
        else:
            return render(request, 'auth/login.html',
                          {'error': 'Login Failed.'})

    return render(request, 'auth/login.html')


def user_logout(request):
    logout(request)
    return redirect('/login/')
