from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages import add_message
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth.decorators import login_required
from app.models import User


def index(request):

    return render(request, "index.html")


# class UserView(generic.TemplateView):
#     template_name


def auth_user(request):
    if request.method == "GET":
        return render(request, "login.html")

    username = request.POST.get("username") or None
    password = request.POST.get("password") or None

    user = authenticate(username=username, password=password)

    print(user)
    if user is not None:
        login(request, user)
        return redirect("profile")
    else:
        add_message(request, messages.WARNING, "INVALID USERNAME OR PASSWORD")
        return render(request, "login.html")


def pricing(request):
    from .models import Pricing

    data = {
        "pricing": Pricing.objects.all()
    }

    return render(request, "pricing.html", context=data)


def register(request):
    if request.method == "GET":
        return render(request, "register.html")

    first_name = request.POST.get("fname") or None
    last_name = request.POST.get("lname") or None
    username = request.POST.get("uname") or None
    email = request.POST.get("email") or None
    phone = request.POST.get("number") or None
    addy = request.POST.get("addy") or None
    password = request.POST.get("pass") or None

    try:
        user = User()
        user.first_name = first_name
        user.last_name = last_name
        user.address = addy
        user.username = username
        user.phone_number = phone
        user.email = email
        user.set_password(password)
        user.save()
        add_message(request, messages.INFO, "Registration complete please login")
        return redirect("login")
    except Exception as e:
        add_message(request, messages.WARNING, "Please complete the form ")
        return render(request, "register.html")


def profile(request):
    return render(request, "profile.html")


def projects(request):

    return render(request, "projects.html")

@login_required()
def new_project(request):
    
    return render(request, "new_project.html")


def logout_user(request):
    logout(request)
    return redirect("home")
