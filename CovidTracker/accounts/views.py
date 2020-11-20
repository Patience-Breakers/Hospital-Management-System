from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import patient

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
            return redirect('dashboard')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
def buttons(request):
    if request.method == 'POST':
        pat =patient()
        pat.name = request.POST['name']
        pat.age = request.POST['age']
        pat.gender = request.POST['gender']
        pat.temperature = request.POST['temperature']
        pat.o2level = request.POST['o2level']
        pat.date = request.POST['date']
        pat.address = request.POST['address']
        if 'symptoms' in request.POST:
            pat.symptoms = request.POST['symptoms']
        else:
            is_private = False
        
        if 'existingdisease' in request.POST:
            pat.existingdisease = request.POST['existingdisease']
        else:
            is_private = False
        
        if 'status' in request.POST:
            pat.status = request.POST['status']
        else:
            is_private = False
        pat.save()
        messages.info(request, 'User Created')
        return redirect('index')
    else:
        return render(request, '3buttons.html')

