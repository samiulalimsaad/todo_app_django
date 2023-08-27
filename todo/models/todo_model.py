from django.db import models

from todo.enums.status_enum import StatusEnum


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    due_date = models.DateTimeField("due date")
    status = models.CharField(
        max_length=20, choices=StatusEnum, default=StatusEnum.Pending
    )
