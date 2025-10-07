# registration/views.py

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegistrationSerializer # Note: Using RegistrationSerializer

@api_view(['POST'])
def register_user(request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        # Return only a subset of data (exclude password, which is write-only)
        return Response(serializer.data, status.HTTP_201_CREATED) 
    
    # Return 400 with validation errors if data is invalid
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)