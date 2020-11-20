from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def index(request):
    return render(request, 'index.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index.html')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login.html')
    else:
        return render(request,'login.html')
