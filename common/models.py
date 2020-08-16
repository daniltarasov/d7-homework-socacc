from django.db import models
from django.contrib.auth.models import User  
from allauth.socialaccount.models import SocialAccount
# from SocialAccount.fields import JSONField
# import json
# Create your models here.

  
  
class UserProfile(models.Model):  
  
    age = models.IntegerField()  
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', blank=True)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=20)


