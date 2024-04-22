from django.db import models
from apps.core.models import AbstractBaseModel
# Create your models here.
EDUCATION_LEVELS = (
    ("University", "University"),
    ("College", "College"),
    ("Secondary School", "Secondary School"),
    ("Primary School", "Primary School"),
)

class Specialist(AbstractBaseModel):
    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
    specialization = models.CharField(max_length=255)
    hourly_rate = models.DecimalField(max_digits=100, decimal_places=2)
    services = models.JSONField(default=list)
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    

class SpecialistEducation(AbstractBaseModel):
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
    education_level = models.CharField(max_length=255, choices=EDUCATION_LEVELS)
    school_name = models.CharField(max_length=255)
    start_year = models.CharField(max_length=255)
    graduation_year = models.CharField(max_length=255)
    certificate = models.FileField(upload_to="education_certificates/", null=True, blank=True)

    def __str__(self):
        return self.specialist.user.username 
    

class SpecialistCertification(AbstractBaseModel):
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    certificate_number = models.CharField(max_length=255, null=True)
    certificate_url = models.URLField(null=True)
    certificate = models.FileField(upload_to="specialist_certificates/", null=True)

    def __str__(self):
        return self.title
