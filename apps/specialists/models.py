from django.db import models
from apps.core.models import AbstractBaseModel
# Create your models here.
class Specialist(AbstractBaseModel):
    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
    specialization = models.CharField(max_length=255)
    