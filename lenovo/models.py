from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserInfo(AbstractUser):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=11, null=True, unique=True)