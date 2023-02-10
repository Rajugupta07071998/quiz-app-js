from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):
    #id=serializers.IntegerField()
    username=serializers.CharField(max_length=100)
    email=serializers.EmailField(max_length=100)

    def create(self,validate_data):
        return User.objects.create(**validate_data)
    