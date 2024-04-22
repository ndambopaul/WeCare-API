from rest_framework import serializers
from apps.specialists.models import Specialist
from apps.users.models import User


class CreateSpecialistSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    id_number = serializers.CharField(max_length=255)
    date_of_birth = serializers.DateField()
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255)
    gender = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(max_length=255)
    specialization = serializers.CharField(max_length=255)
    hourly_rate = serializers.DecimalField(max_digits=100, decimal_places=2)
    postal_address = serializers.CharField(max_length=255)
    physical_address = serializers.CharField(max_length=255)
    town = serializers.CharField(max_length=255)
    county = serializers.CharField(max_length=255)
    country = serializers.CharField(max_length=255)
    profile_photo = serializers.FileField()

    def create(self, validated_data):
        user = User.objects.create(
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            id_number=validated_data.get('id_number'),
            date_of_birth=validated_data.get('date_of_birth'),
            username=validated_data.get("username"),
            email=validated_data.get("email"),
            gender=validated_data.get("gender"),
            phone_number=validated_data.get("phone_number"),
            postal_address=validated_data.get("postal_address"),
            physical_address=validated_data.get("physical_address"),
            county=validated_data.get("county"),
            town=validated_data.get('town'),
            country = validated_data.get("country")
        )
        user.set_password(validated_data.get('password'))
        user.save()
        Specialist.objects.create(
            user=user, 
            specialization=validated_data.get("specialization"),
            hourly_rate=validated_data.get("hourly_rate")
        )
        return user

class SpecialistSerializer(serializers.ModelSerializer):
    user_details = serializers.SerializerMethodField()
    class Meta:
        model = Specialist
        fields = "__all__"
    
    def get_user_details(self, obj):
        return User.objects.filter(id=obj.user.id).values().first()