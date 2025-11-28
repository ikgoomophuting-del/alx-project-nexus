from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_ROLES = (
        ("customer", "Customer"),
        ("seller", "Seller"),
        ("admin", "Admin"),
    )

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=USER_ROLES, default="customer")
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # username is optional

    def __str__(self):
        return f"{self.email} ({self.role})"
