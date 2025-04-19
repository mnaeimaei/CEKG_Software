from django.contrib import admin
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)

    def approve_user(self, request, queryset):
        for profile in queryset:
            profile.is_approved = True
            profile.save()
            send_mail(
                'Your Account Has Been Approved',
                'Your account has been approved. You can now log in.',
                settings.DEFAULT_FROM_EMAIL,
                [profile.user.email],  # Corrected line
            )

    approve_user.short_description = "Approve selected users"
    actions = [approve_user]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_email', 'organization', 'is_approved')
    list_filter = ('is_approved',)
    search_fields = ('user__username', 'user__email', 'organization')
    actions = ['approve_user']

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'  # Optional: Custom column header

    def approve_user(self, request, queryset):
        for profile in queryset:
            profile.is_approved = True
            profile.save()
            send_mail(
                'Your Account Has Been Approved',
                'Your account has been approved. You can now log in.',
                settings.DEFAULT_FROM_EMAIL,
                [profile.user.email],
            )

    approve_user.short_description = "Approve selected users"
