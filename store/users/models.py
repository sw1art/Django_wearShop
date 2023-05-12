from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

GENDER_CHOICES = [
('M', 'Male'),
('F', 'Female'),
('O', 'Other')
]
class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, null=True, blank=True)