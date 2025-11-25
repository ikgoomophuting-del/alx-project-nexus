from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)

    ROLE_CHOICES = (
        ("admin","Admin"),
        ("seller","Seller"),
        ("customer","Customer"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="customer")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
