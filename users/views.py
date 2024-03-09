from django.http import HttpResponse
from rest_framework.mixins import ListModelMixin

from .serializers import UserModelSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserModel
from rest_framework import status


def say_hello(request):
    return HttpResponse('<h1>Hello World</h1>')


class RegistrationApiView(APIView):
    def post(self, request):
        serializer = UserModelSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginApiView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')

        if not username or not password:
            return Response({'Error': 'Blank or Incorrect Username or Password'}, status=status.HTTP_404_NOT_FOUND)

        user = UserModel.objects.filter(username=data['username']).first()
        if not user:
            return Response({'Error': 'Incorrect username or password'},
                            status=status.HTTP_404_NOT_FOUND)

        if not user.check_password(data['password']):
            return Response({'Error': 'Incorrect username or password'},
                            status=status.HTTP_404_NOT_FOUND)

        success = {
            "Success": "Successfully, Login"
        }
        return Response(success, status=status.HTTP_200_OK)


class ListUsersApiView(APIView, ListModelMixin):
    def get(self, request, *args, **kwargs):
        queryset = UserModel.objects.all()
        serializer = UserModelSerializers(queryset, many=True)
        return Response(serializer.data)
