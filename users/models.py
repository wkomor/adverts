from django.db import models
from django.contrib.auth.models import AbstractUser


class AppUser(AbstractUser):
    """
    Model for user with simple roles
    """
    ROLES = (('Advertiser', 'Рекламодатель'), ('Admin', 'Администратор'))

    role = models.CharField(max_length=16, choices=ROLES)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username