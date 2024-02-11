from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.CharField(max_length=255)  
    mobile = models.CharField(max_length=20)  
    otp = models.CharField(max_length=6)


class user(models.Model):
    phone_number = models.CharField(max_length=12, unique=True)
    is_phone_verfied = models.BooleanField(default=False)
    opt = models.CharField(max_length=6)

    

