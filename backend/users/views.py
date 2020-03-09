
from django.shortcuts import render
from rest_framework import viewsets          
from .serializers import UserSerializer      
from .models import NuUser                 

class UserView(viewsets.ModelViewSet):       
    serializer_class = UserSerializer          
    queryset = NuUser.objects.all() 