from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import User

class HelloSerializer(serializers.Serializer):
    hello = serializers.CharField()




class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ['id', 'username']