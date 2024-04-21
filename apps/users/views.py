from django.shortcuts import render
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.serializers import RegisterUserSerializer, LoginUserSerializer, UserActivationSerializer, ChangePasswordSerializer, ForgotPasswordSerializer

from apps.users.models import User

# Create your views here.
class RegisterUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUserAPIView(ObtainAuthToken):
    serializer_class = LoginUserSerializer
    permission_classes = [AllowAny]

    def get_serializer(self):
        return self.serializer_class()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token = Token.objects.get(user=user).key

        # Update last_login of the current user
        user.last_login = timezone.now()
        user.save()

        response = {
            "token": token,
            "pk": user.pk,
            "role": user.role,
            "username": user.username,
            "email": user.email,
            "name": f"{user.first_name} {user.last_name}",
        }

        return Response(response)
    


class ForgotPasswordAPIView(APIView):
    serializer_class = ForgotPasswordSerializer
    permission_classes = [
        AllowAny,
    ]
    def get_serializer_class(self):
        return self.serializer_class()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.send_email()

        return Response(
            {"message": "Password reset link will be send to your email!"},
            status=status.HTTP_200_OK,
        )


class ChangePasswordAPIView(APIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [
        AllowAny,
    ]

    def get_serializer_class(self):
        return self.serializer_class()

    def post(self, request, token):
        context = {"request": request, "token": token}
        serializer = self.serializer_class(data=request.data, context=context)
        if serializer.is_valid():
            serializer.save(serializer.validated_data)
            return Response(
                {"message": "Password has been successfully changed"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserActivationAPIView(APIView):
    serializer_class = UserActivationSerializer
    permission_classes = [
        AllowAny,
    ]

    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid(raise_exception=True):
            user = User.objects.get(token=data["token"])
            user.is_active = True
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
