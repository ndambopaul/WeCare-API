from django.urls import path

from apps.users.views import LoginUserAPIView, RegisterUserAPIView, ForgotPasswordAPIView, ChangePasswordAPIView, UserActivationAPIView

urlpatterns = [
    #path("", UsersListAPIView.as_view(), name="users"),
    #path("<int:pk>/", UserProfileAPIView.as_view(), name="user-profile"),
    path("register/", RegisterUserAPIView.as_view(), name="register"),
    path("login/", LoginUserAPIView.as_view(), name="login"),
    path("forgot-password/", ForgotPasswordAPIView.as_view(), name="forgot-password"),
    path("change-password/<str:token>/", ChangePasswordAPIView.as_view(), name="change-password"),
    path("activate-user/", UserActivationAPIView.as_view(), name="activate-user"),
    
]
