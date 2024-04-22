from datetime import datetime

from django.contrib.auth import authenticate
from django.utils import timezone
from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.exceptions import AuthenticationFailed

from apps.core.validators import check_valid_password
from apps.users.models import User
from apps.users.utils import generate_unique_key

class UusersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

        extra_kwargs = {"password": {"write_only": True}}

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "gender",
            "phone_number",
            "id_number",
            "date_of_birth",
            "role",
            "town",
            "country",
            "password",
        ]

        extra_kwargs = {"password": {"write_only": True}}


class LoginUserSerializer(AuthTokenSerializer):
    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                if not user.is_active:
                    raise serializers.ValidationError("User account is disabled.", code="authorization")
            else:
                raise AuthenticationFailed("Unable to log in with provided credentials.", code="authorization")
        else:
            raise serializers.ValidationError('Must include "username" and "password".', code="authorization")
        
        attrs["user"] = user
        return attrs



class ChangePasswordSerializer(serializers.Serializer):
    user = None
    password = serializers.CharField()
    repeat_password = serializers.CharField()

    def save(self, validated_data):
        self.user.set_password(validated_data["password"])
        self.user.token = None
        self.user.token_expiration_date = None
        if not self.user.is_active:
            self.user.activation_date = datetime.date.today()
        self.user.is_active = True
        self.user.save()

    def validate(self, data):
        self.check_valid_token()
        check_valid_password(data, user=self.user)

        return data

    def check_valid_token(self):
        try:
            self.user = User.objects.get(token=self.context["token"])
        except User.DoesNotExist:
            raise serializers.ValidationError("Token is not valid.")
        fields = "__all__"



class UserActivationSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=500)


class ForgotPasswordSerializer(serializers.Serializer):
    user = None
    email = serializers.EmailField()

    def send_email(self):
        self.user.token = generate_unique_key(self.user.email)
        self.user.token_expiration_date = timezone.now() + timezone.timedelta(hours=24)
        self.user.IS_UPDATE = True
        self.user.save()
        #reset_mail(self.user)

    def validate_email(self, value):
        try:
            self.user = User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("No user found with provided email!")
