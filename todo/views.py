from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout as logout_user, login as login_user
from todo.enums.status_enum import StatusEnum

from todo.models import Todo


# Create your views here.


@login_required(login_url="login/")
def index(req) -> HttpResponse:
    if req.user.is_authenticated:
        user = req.user
        if req.method == "POST":
            print(user)
            todo = Todo(
                user=user,
                title=req.POST["title"],
                description=req.POST["description"],
                due_date=req.POST["due_date"],
                status=StatusEnum.Pending,
            )
            print(todo)
            todo.save()
            todos = Todo.objects.filter(user=user)
            return render(req, "todo.html", {"is_authenticated": True, "todos": todos})
        else:
            todos = Todo.objects.filter(user=user)
            print(todos)
            return render(req, "todo.html", {"is_authenticated": True, "todos": todos})
    else:
        return render(req, "login.html", {"is_authenticated": False})


def todo_detail(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    return render(request, "todo_detail.html", {"todo": todo})


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
