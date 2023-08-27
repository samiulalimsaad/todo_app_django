import email
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout as logout_user, login as login_user


# Create your views here.


@login_required(login_url="login/")
def index(req) -> HttpResponse:
    if req.user.is_authenticated:
        user = User.objects.get()
        print(req.user)
        # Do something for authenticated users.
        ...
        return render(req, "todo.html", {"is_authenticated": True})
    else:
        # Do something for anonymous users.
        ...
        return render(req, "login.html", {"is_authenticated": False})


def register(request) -> HttpResponse:
    if request.method == "POST":
        print("request.POST")
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = User.objects.create_user(name, email, password)
        # user.has_perm('foo.add_bar')
        user.save()
        return redirect("login")

    return render(request, "signup.html")


def login(request) -> HttpResponse:
    if request.method == "POST":
        print(request.POST["name"], request.POST["password"])
        user = authenticate(
            request, username=request.POST["name"], password=request.POST["password"]
        )
        print(user)
        if user is not None:
            login_user(request, user)
            return redirect("index")
        else:
            # No backend authenticated the credentials
            ...

    return render(request, "login.html")


def logout(request) -> HttpResponse:
    logout_user(request)
    return redirect("login")
