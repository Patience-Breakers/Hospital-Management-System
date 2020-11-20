from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import patient

# Create your views here.
def index(request):
    if request.method == 'POST':
        pat =patient()
        pat.name = request.POST['name']
        pat.age = request.POST['age']
        pat.gender = request.POST['gender']
        pat.temperature = request.POST['temperature']
        pat.o2level = request.POST['o2level']
        pat.date = request.POST['date']
        pat.address = request.POST['address']
        pat.symptoms = request.POST['sympomts']
        pat.existingdisease = request.POST['existingdisease']
        pat.status = request.POST['status']
        pat.save()
    return render(request, 'index.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
