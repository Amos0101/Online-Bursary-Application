
from django.contrib.auth import  logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Validate passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        # Check if user exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already taken")
            return redirect('register')

        # Save user
        user = User(username=username, email=email, password=make_password(password1))
        user.save()

        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')

    return render(request, 'register.html')


def student_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')



# Logout
def student_logout(request):
    logout(request)
    return redirect('login')
@login_required()
def home(request):
    return render(request, 'homepage.html')


def admin_register(request):
    if request.method == "POST":
        employee_number = request.POST["employee_number"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect("admin_register")

        if User.objects.filter(username=employee_number).exists():
            messages.error(request, "Employee number already exists.")
            return redirect("admin_register")

        user = User.objects.create_user(username=employee_number, email=email, password=password1)
        user.save()
        messages.success(request, "Admin registered successfully. Please login.")
        return redirect("admin_login")

    return render(request, "admin_register.html")


#
def admin_login(request):
    if request.method == "POST":
        employee_number = request.POST["employee_number"]
        password = request.POST["password"]

        user = authenticate(request, username=employee_number, password=password)
        if user is not None:
            login(request, user)
            return redirect("admin_home")
        else:
            messages.error(request, "Invalid credentials.")
            return redirect("admin_login")

    return render(request, "admin_login.html")
@login_required()
def admin_home(request):
    return render(request, "admin_home.html")

