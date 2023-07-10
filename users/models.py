from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to="users_images", height_field=None, width_field=None, max_length=None)