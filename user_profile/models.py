from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.mail import EmailMessage
from django.conf import settings
from django.db import models
from django import forms

class User:
    username = models.CharField(unique=True, max_length=100)
    password = forms.CharField(widget = forms.PasswordInput, max_length = 16)
    email = models.EmailField(unique=True, max_length=255)
    birth_date = models.DateTimeField(auto_now_add=True)

