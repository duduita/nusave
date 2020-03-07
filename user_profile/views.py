from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse

CATEGORYS = ['Alimentação',
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

class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponse(f'login {request.user.email}')

        # else, return front profile
    def post(self, request, *args, **kwargs):
        account_number = request.POST['account_number']
        password = request.POST['password']

        user = authenticate(account_number = account_number, password= password)

        if user:
            login(request, user)

        return JsonResponse({'success': user is not None})

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponse(f'logout {request.user.email}')

