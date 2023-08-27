from django.utils import timezone
from django.db import models

from todo.enums.status_enum import StatusEnum


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Todo(TimeStampMixin):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    due_date = models.DateTimeField("due date")
    status = models.CharField(
        max_length=20, choices=StatusEnum.choices, default=StatusEnum.Pending
    )

    def __str__(self) -> str:
        return self.title


class User(TimeStampMixin):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    todos = models.ForeignKey(Todo, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.name
