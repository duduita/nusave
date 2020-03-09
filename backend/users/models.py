from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.mail import EmailMessage
from django.conf import settings
from django.db import models

CATEGORIES = ['Alimentação',
             'Assinatura e serviços',
             'Educacao',
             'Saude',
             'Roupas',
             'Transporte',
             'Saques',
             'Outros']

FILTER = ['Classe social',
          'Idade',
          'Região',
          'Profissão']

          
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


class NuUser(models.Model):
    account_number = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True, max_length=255)

    name = models.CharField(default = "", max_length = 100)
    marital_status = models.CharField(default = "", max_length = 100)
    gender = models.CharField(max_length = 100,default = "")
    social_class = models.CharField(max_length = 100,default = "")
    age = models.IntegerField(default= 0)
    dependents = models.IntegerField(default = 0)
    region = models.CharField(max_length = 100,default = "")
    date = models.CharField(max_length = 100,default = "")
    food_expense = models.FloatField(default= 0)
    services_expense = models.FloatField(default= 0)
    education_expense = models.FloatField(default= 0)
    restaurants_expense = models.FloatField(default= 0)
    house_expense = models.FloatField(default= 0)
    debts_expense = models.FloatField(default= 0)
    investiments_expense = models.FloatField(default= 0)
    recreation_expense = models.FloatField(default= 0)
    health_expense = models.FloatField(default= 0)
    transport_expense = models.FloatField(default= 0)
    beauty_expense = models.FloatField(default= 0)
    others_expense = models.FloatField(default= 0)
    


    def __str__(self):
        return self.name
        
class Profile(NuUser):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.initial_money = 0
        self.badges = []
        self.warning = []

class Person(Profile):
    def __init__(self):
        super().__init__()
        self.food = []
        self.services = []
        self.education = []
        self.health = []
        self.transport = []
        self.withdrawal = []
        self.others = []

class Expense:
    def __init__(self, value, date):
        self.value = value
        self.date = date

