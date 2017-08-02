from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.messages import add_message
from django.contrib import messages


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
        return render(request, "index.html")
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
        return render(request,"register.html")

def profile(request):
    return render(request,"profile.html")