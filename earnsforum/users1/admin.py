from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_admin', 'is_moderator', 'user_date_joined')
    list_filter = ('is_admin', 'is_moderator', 'user__date_joined')
    search_fields = ('user__username', 'user__email')

    def user_date_joined(self, obj):
        return obj.user.date_joined
    user_date_joined.admin_order_field = 'user__date_joined'
    user_date_joined.short_description = 'Date Joined'