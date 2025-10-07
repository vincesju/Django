# registration/serializers.py

from rest_framework import serializers
from django.contrib.auth.hashers import make_password  # <-- Import for hashing
from .models import UserRegistration

class RegistrationSerializer(serializers.ModelSerializer):
    # Set password as write-only so it's not exposed in responses
    password = serializers.CharField(write_only=True) 

    class Meta:
        model = UserRegistration
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'gender') 
        # Optional: Add extra validation/error handling for email
        extra_kwargs = {
            'email': {'required': True, 'allow_blank': False}
        }

    # Override the create method to hash the password
    def create(self, validated_data):
        # 🔑 Hash the incoming plain-text password
        validated_data['password'] = make_password(validated_data['password'])
        
        # Save the user instance with the HASHED password
        user = UserRegistration.objects.create(**validated_data)
        return user