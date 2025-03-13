from django.db import models
from django.contrib.auth.models import AbstractUser

class Student(AbstractUser):
    username = models.CharField(max_length=191, unique=True)  # Registration number
    email = models.EmailField(unique=True)

    # Fix clashes by setting related_name attributes
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="student_groups",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="student_permissions",
        blank=True
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username



