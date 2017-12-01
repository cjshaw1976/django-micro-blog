from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import Profile


User = get_user_model()
admin.site.unregister(User)

# Add the user profile to the users admin area
class InlineProfile(admin.StackedInline):
    model = Profile

# Create a custom user admin area to incorporate the profile
class CustomAdmin(UserAdmin):
    date_hierarchy = 'date_joined'
    inlines = [InlineProfile, ]
    list_display = list(UserAdmin.list_display) + ['email_confirmed']

    def email_confirmed(self, obj):
        return obj.userProfile.email_confirmed

admin.site.register(User, CustomAdmin)
