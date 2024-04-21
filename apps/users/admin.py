from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from apps.users.models import User


# Register your models here.
class UserAdmin(BaseUserAdmin):
    list_display = ["id", "username", "id_number", "email", "phone_number", "token", "gender", "role"]
    search_fields = ('username', 'email', 'first_name', 'last_name')


#admin.site.unregister(User)
admin.site.register(User, UserAdmin)
