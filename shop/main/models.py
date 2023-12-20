
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
import random
class Login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=10)
    class Meta:
        db_table="Login"

class User_Custom(AbstractUser):
    phone_number=models.CharField(max_length=15)





