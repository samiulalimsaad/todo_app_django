from django.utils import timezone
from django.db import models
from todo.enums.status_enum import StatusEnum
from django.contrib.auth.models import User


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Todo(TimeStampMixin):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    due_date = models.DateTimeField("due date")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    status = models.CharField(
        max_length=20, choices=StatusEnum.choices, default=StatusEnum.Pending
    )

    def __str__(self) -> str:
        return self.title
