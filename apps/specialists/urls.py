from django.urls import path
from apps.specialists.views import CreateSpecialistAPIView, SpecialistAPIView

urlpatterns = [
    path("", SpecialistAPIView.as_view(), name="specialists"),
    path("create-specialist/", CreateSpecialistAPIView.as_view(), name="create-specialist"),
]