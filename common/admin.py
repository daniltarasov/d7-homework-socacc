from django.contrib import admin

# Register your models here.
from common.models import UserProfile
# Register your models here.


@admin.register(UserProfile)  
class ProfileAdmin(admin.ModelAdmin):  
    # pass
    @staticmethod
    def profile_name(obj):
        # return obj.User.username
        return obj.user.username

    list_display = ['profile_name']

