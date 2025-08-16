from django.contrib.admin.decorators import register
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from account.models import User


@register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "id",
        "get_full_name",
        "email",
    )
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")})
    )
