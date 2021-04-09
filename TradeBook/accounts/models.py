from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# TODO: may be AbstractUser for Profile


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True, default=0)

    def __str__(self):
        return self.first_name


class SocialNetwork(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.name
