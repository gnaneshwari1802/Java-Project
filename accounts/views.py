from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.'
# from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate user
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)  # Log the user in
            return redirect("/")  # Redirect to homepage or dashboard
        else:
            messages.info(request, 'Invalid credentials')  # Error message
            return redirect('login')  # Stay on the login page
    else:
        return render(request, 'login.html')  # Render the login page if it's a GET request

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']  # Fix the field name here
        email = request.POST['email']

        if password1 == password2:  # Check if passwords match
            if User.objects.filter(username=username).exists():  # Check if username is taken
                messages.info(request, 'Username is already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():  # Check if email is taken
                messages.info(request, 'Email is already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, 
                    password=password1, 
                    email=email, 
                    first_name=first_name, 
                    last_name=last_name
                )
                user.save()
                print('User created')  # Optional: for debugging purposes
                return redirect('login')  # Redirect to login after successful registration
        else:
            messages.info(request, 'Passwords do not match')  # Error message
            return redirect('register')  # Stay on the register page

    else:
        return render(request, 'register.html')  # Render the register page if it's a GET request

def logout(request):
    auth.logout(request)  # Logout the user
    return redirect('/')  # Redirect to the homepage or login page
