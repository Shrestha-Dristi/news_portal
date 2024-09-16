from rest_framework import serializers
from django.contrib.auth.models import User

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['username', 'email', 'first_name']
        # fields = '__all__'
        exclude = ['password']