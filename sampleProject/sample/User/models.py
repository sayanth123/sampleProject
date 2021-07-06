from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from .forms import RegisterForm

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     email=models.EmailField(max_length=200,unique=True)
#     first_name=models.CharField(max_length=60)
#     last_name=models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.user

class Post(models.Model):
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return str(self.user)
