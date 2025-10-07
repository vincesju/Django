from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from .models import UserRegistration 

@api_view(['POST'])
def register_user(request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED) 
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ADD THIS NEW FUNCTION
@api_view(['GET'])
def get_users(request):
    users = UserRegistration.objects.all()
    serializer = RegistrationSerializer(users, many=True)
    return Response(serializer.data)