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

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk): 
    try:
        user = UserRegistration.objects.get(pk=pk)
    except UserRegistration.DoesNotExist:
        return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RegistrationSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RegistrationSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)