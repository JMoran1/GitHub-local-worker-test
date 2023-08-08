from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserType(models.TextChoices):
    ADMIN = 'A', 'Admin',
    STANDARD = 'S', 'Standard'

class User(AbstractUser):
    UserType = UserType

    user_type = models.CharField(
        max_length=1,
        choices=UserType.choices,
        default=UserType.STANDARD,
    )