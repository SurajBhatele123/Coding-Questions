from rest_framework import serializers
from jwtapp.models import  Authentication

class AuthenticationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authentication
        fields = ('id',
                  'emailid',
                  'password',
                )

