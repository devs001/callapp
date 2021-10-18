from django.db import models
from callapp import settings
# Create your models here.
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=1)
    phone = models.CharField(max_length=14,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
