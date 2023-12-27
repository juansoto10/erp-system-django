"""Users app views"""
from django.shortcuts import render, redirect

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CreateUserForm, LoginForm


# test
def test(request):
    
    return render(request, 'production/index.html')


# Register a user
def register(request):
    
    form = CreateUserForm()

    if request.method == "POST":
        
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            messages.success(request, 'Account created successfully')
            
            return redirect('my-login')
        
    context = {'form': form}
    
    return render(request, 'webapp/register.html', context=context)
            
            
# Login a user
def my_login(request):
    
    form = LoginForm()
    
    if request.method == 'POST':
        
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            
            username = request.POST.get('username')
            password = request.POST.get('password')
    
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                
                auth.login(request, user)
                
                return redirect('dashboard')
                
    context = {'form': form}
    
    return render(request, 'webapp/login.html', context=context)


# User logout
def user_logout(request):
    
    auth.logout(request)
    
    messages.success(request, 'You have logged out')
    
    return redirect('my-login')
