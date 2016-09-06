# created by Vitold Komorovski
# 06.09.2016
from django.db import models
from django_extensions.db.models import TimeStampedModel
from hitcount.models import HitCountMixin


class Ad(TimeStampedModel, HitCountMixin):
    """
    Basic model for ad
    """
    title = models.CharField(verbose_name='Заголовок', max_length=255,
                             db_index=True)
    text = models.TextField(verbose_name="Текст объявления")
    is_active = models.BooleanField(default=True)
    lifetime = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "Ad"
