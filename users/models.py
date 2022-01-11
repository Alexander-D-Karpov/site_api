from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Person(AbstractUser):
    username = models.CharField(unique=True, blank=False, max_length=100)
    email = models.EmailField(blank=False, unique=True, max_length=150)
    first_name = models.CharField(blank=True, max_length=100)
    last_name = models.CharField(blank=True, max_length=100)
    about = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to="user_icons/")

    class Meta:
        db_table = "Users"

    def __str__(self):
        return self.username
