from rest_framework import serializers
from django.contrib.auth.models import User

class UserCreateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=3, write_only=True)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)