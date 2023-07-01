from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer


class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.user.auth_token.delete()
        return Response(
            data={'message': f'Bye {request.user.username}!'},
            status=status.HTTP_204_NO_CONTENT
        )

class UserRegistration(generics.CreateAPIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        userSerializer = UserSerializer(data=request.data)
        if userSerializer.is_valid():
            temp = {}
            for key, value in request.data.items():
                temp[key] = value
            userSerializer.create(temp)
            return Response({'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)
        return Response({'message': userSerializer.errors})
