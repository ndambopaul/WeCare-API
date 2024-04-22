from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


from django.contrib.auth.models import AbstractUser
from apps.core.models import AbstractBaseModel
# Create your models here.
USER_ROLES = (
    ("Admin", "Admin"),
    ("Manager", "Manager"),
    ("Doctor", "Doctor"),
    ("Patient", "Patient"),
)

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)
USER_STATUS_CHOICES = (
    ("Active", "Active"),
    ("Suspended", "Suspended"),
    ("Deactivated", "Deactivated"),
)

class User(AbstractUser, AbstractBaseModel):
    role = models.CharField(max_length=255, choices=USER_ROLES)
    phone_number = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(null=True)
    postal_address = models.CharField(max_length=255, null=True)
    physical_address = models.CharField(max_length=255, null=True)
    town = models.CharField(max_length=255, null=True)
    county = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    token = models.CharField(null=True, max_length=255)
    token_expiration_date = models.DateTimeField(null=True)
    activation_date = models.DateTimeField(null=True)
    status = models.CharField(max_length=255, choices=USER_STATUS_CHOICES, default="Active")
    

    def __str__(self):
        return self.username

    def name(self):
        return f"{self.first_name} {self.last_name}"


@receiver(post_save, sender=User)
def create_user_token(sender, instance, created, **kwargs):
    if created:
        token = Token.objects.create(user=instance)
        instance.token = token.key
        instance.set_password(instance.password)
        instance.save()