from django.db import models
from django.contrib.auth.models import User


class AppUser(User):
    """
    Model for user with simple roles
    """
    ROLES = (('Advertiser', 'Рекламодатель'), ('Admin', 'Администратор'))

    role = models.CharField(max_length=16, choices=ROLES)
