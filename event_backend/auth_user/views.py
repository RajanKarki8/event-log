from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegisterForm

def UserRegister(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.save()
            messages.success(request, 'username created successfully!')
            return redirect('login')
    else:
        form =RegisterForm()
    context = {
        'form':form
    }
    return render(request, 'auth_user/register.html', context)

def Userlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
           messages.info(request, 'user does not exits')
        user = authenticate(username = username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successfully! Welcome to the speech event')
            return redirect('index')
        else:
            messages.info(request, 'username or password is incorrect')
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'auth_user/login.html', context)

def Userlogout(request):
    logout(request)
    messages.info(request, 'you have been logout!')
    return redirect('index')
        