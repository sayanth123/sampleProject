from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from .forms import RegisterForm



class Post(models.Model):
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return str(self.user)
