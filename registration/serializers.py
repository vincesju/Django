# registration/serializers.py

from rest_framework import serializers
from django.contrib.auth.hashers import make_password  
from .models import UserRegistration

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) 

    class Meta:
        model = UserRegistration
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'gender') 
        extra_kwargs = {
            'email': {'required': True, 'allow_blank': False}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = UserRegistration.objects.create(**validated_data)
        return user

    # === ADD ONLY THIS METHOD ===
    def update(self, instance, validated_data):
        # Handle password - only hash if provided
        password = validated_data.pop('password', None)
        if password:
            validated_data['password'] = make_password(password)
        
        # Update other fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance
    # === END OF ADDED METHOD ===