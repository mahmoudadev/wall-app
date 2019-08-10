from django.contrib.auth.models import User
from rest_framework import serializers




class UserAuthSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email']



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
        ]