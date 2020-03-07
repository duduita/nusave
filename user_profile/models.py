from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.mail import EmailMessage
from django.conf import settings
from django.db import models


class AuthUserManager(BaseUserManager):
    def create_user(self, account_number, email, password=None):
        if not account_number:
            raise ValueError('Users must have an account number')
        if not email:
            raise ValueError('Users must have a email')

        user = self.model(account_number=account_number,
                          email=self.normalize_email(email))

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, *args, **kwargs):
        return self.create_user(*args, **kwargs)


class NuUser(AbstractBaseUser, PermissionsMixin):
    account_number = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True, max_length=255)
    date_joined = models.DateTimeField(auto_now_add=True)
    birth_date = models.DateTimeField(auto_now_add=True)

    objects = AuthUserManager()
    ACCOUNT_NUMBER_FIELD = 'account_number'
    REQUIRED_FIELDS = ['email']
