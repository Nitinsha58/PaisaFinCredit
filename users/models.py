from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from django.db import models

class User(AbstractBaseUser, PermissionsMixin):
    id = models.IntegerField(primary_key=True)
    phone = models.CharField(max_length=10, unique=True)
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    otp = models.CharField(null=True, blank=True, max_length=6)
    terms_accepted = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager() 

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []