from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status, generics

from apps.specialists.serializers import CreateSpecialistSerializer, SpecialistSerializer
from apps.specialists.models import Specialist
# Create your views here.
class CreateSpecialistAPIView(generics.CreateAPIView):
    serializer_class = CreateSpecialistSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    

class SpecialistAPIView(generics.ListAPIView):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializer
