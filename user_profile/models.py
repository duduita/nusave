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

class AdvancedUser(User):
    def __init__(self):
        self.gross_monthly_income = None
        self.investment_suggestion = None
        self.level = None
        self.extern_evaluation = None
        self.social_class = None
        self.region = None
        self.person_profile = None
        self.age = None
        self.likes = None
        self.month_save_suggestion = None
        self.badges = []
