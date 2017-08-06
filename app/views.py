from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages import add_message
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib.auth.decorators import login_required
from app.models import User, Payment, Document, PrintJob


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
        add_message(request, messages.INFO,
                    "Registration complete please login")
        return redirect("login")
    except Exception as e:
        add_message(request, messages.WARNING, "Please complete the form ")
        return render(request, "register.html")


@login_required()
def profile(request):

    if Payment.objects.filter(payer=request.user, paid=False):
        add_message(request, messages.INFO,
                    "You have outstanding paynemts <a href='/invoice/'>View</a>")

    return render(request, "profile.html")


@login_required()
def projects(request):
    if Payment.objects.filter(payer=request.user, paid=False):
        add_message(request, messages.INFO,
                    "You have outstanding paynemts <a href='/invoice/'>View</a>")

    data = {
        "projects": PrintJob.objects.filter(charged_to=request.user)
    }
    return render(request, "projects.html", data)


@login_required()
def new_project(request):
    if request.method == "GET":
        return render(request, "new_project.html")

    title = request.POST.get('title') or None
    file = request.POST.get('file') or None
    copies = request.POST.get('copies') or None
    brief = request.POST.get('brief') or None

    try:
        """
        Creating and saving a new User.
        """
        doc = Document()
        doc.brief = brief
        doc.title = title
        doc.file = file
        print(doc.file)
        doc.save()

        printjob = PrintJob()
        printjob.charged_to = request.user
        printjob.copies = copies
        printjob.status = "Pending"
        printjob.document = doc

        printjob.save()
        # send_mail(request.user,)

        add_message(request, messages.INFO,
                    "Your Document has been saved sucessfully, and has been sent to the admin for approval")
        return render(request, "new_project.html")
    except Exception as e:
        print(e)
        add_message(request, messages.WARNING,
                    "An error occured, please try again")
        return render(request, "new_project.html")


def logout_user(request):
    # logout the user and redirect home
    logout(request)
    return redirect("home")


@login_required()
def get_invoice(request):

    jobs = PrintJob.objects.filter(charged_to=request.user, status="Approved")
    data = {
        "invoices": jobs
    }
    return render(request, 'invoice.html', data)


def send_mail(user, message):
    # LOgic for sending emails to user aand admin
    pass
