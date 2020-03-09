from rest_framework import serializers
from .models import NuUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NuUser
        fields = '__all__'