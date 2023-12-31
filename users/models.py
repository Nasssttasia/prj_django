from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    photo = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='страна', **NULLABLE)
    code = models.CharField(verbose_name='код', unique=True, **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='активный')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [""]
