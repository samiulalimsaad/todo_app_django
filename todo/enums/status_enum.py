from django.db import models


class StatusEnum(models.TextChoices):
    Pending = "Pending"
    Completed = "Completed"
    In_Progress = "In Progress"
