from django.db import models
from django.contrib.auth.models import AbstractUser
from config import GENDER_CHOICES
# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, null=True, blank=True)