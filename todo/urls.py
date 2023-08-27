from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("todo_detail/<int:todo_id>/", views.todo_detail, name="todo_detail"),
    path("signup/", views.register, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
]
