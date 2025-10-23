from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name = None
    last_name = None

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12, unique=True)
    cnic_no = models.CharField(max_length=15, unique=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username


    

