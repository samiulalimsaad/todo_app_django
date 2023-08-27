from django.db import models

from todo.models.todo_model import Todo


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_created=True)
    todos = models.ForeignKey(Todo, on_delete=models.CASCADE)
