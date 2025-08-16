from admin_numeric_filter.admin import SingleNumericFilter
from django.contrib import admin
from django.contrib.admin import display
from django.urls import reverse
from django.utils.html import format_html
from drf_api_logger_with_user.admin import APILogsAdmin
from drf_api_logger_with_user.models import APILogsModel

from account.models import User


class CustomAPILogsAdmin(APILogsAdmin):
    list_display = APILogsAdmin.list_display + ("user_id",)
    readonly_fields = APILogsAdmin.readonly_fields + ("user",)
    exclude = APILogsAdmin.exclude + ("user_id",)
    list_filter = APILogsAdmin.list_filter + (("user_id", SingleNumericFilter),)

    @display(ordering="user", description="User")
    def user(self, obj):
        user = User.objects.filter(id=obj.user_id).first()
        if not user:
            return "-"
        link = reverse("admin:account_user_change", args=[user.id])
        return format_html("<a href='{url}'>{user}</a>", url=link, user=user)


admin.site.unregister(APILogsModel)
admin.site.register(APILogsModel, CustomAPILogsAdmin)
