from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'other_fields')
    search_fields = ('user__username', 'user__email')
    list_filter = ('user__is_active',)