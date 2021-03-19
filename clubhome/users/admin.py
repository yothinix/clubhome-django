from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from users.forms import UserChangeForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    list_display = ["username", "name", "is_superuser"]
    form = UserChangeForm
    fieldsets = (
        ("User", {
            "fields": ("name","profile_picture", "profile_description", "twitter", "instagram")
        }),
    ) + auth_admin.UserAdmin.fieldsets
