from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AppUser
from .serializers import AppUserSerializer
from iot_app.jwt_manager import JWTManager


class Login(APIView):
    def __init__(self):
        self._jwt_manager = JWTManager()

    def post(self, request, *args, **kwargs):
        data = {'username': request.data.get('username'),
                'password': request.data.get('password')}

        try:
            users = AppUser.objects.filter(
                username=data['username'], password=data['password'])
            if users.count() > 0:
                return Response({'username': data['username'], 'token': self._jwt_manager.create_token(users.first().id)}, status=status.HTTP_200_OK)
        except Exception as e:
            print(str(e))

        return Response("Username or password incorrect", status=status.HTTP_400_BAD_REQUEST)


class Signup(APIView):
    def __init__(self):
        self._jwt_manager = JWTManager()

    def post(self, request, *args, **kwargs):
        data = {'username': request.data.get('username'),
                'password': request.data.get('password')}

        serializer = AppUserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'username': data['username'], 'token': self._jwt_manager.create_token(user.id)}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
