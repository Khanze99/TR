from django.contrib import admin


from .models import Profile, SocialNetwork

# Register your models here.

admin.site.register(Profile)
admin.site.register(SocialNetwork)