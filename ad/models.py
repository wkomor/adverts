# created by Vitold Komorovski
# 06.09.2016
from django.db import models
from django_extensions.db.models import TimeStampedModel
from hitcount.models import HitCountMixin
from users.models import AppUser


class Category(models.Model):
    """
    Ad types
    """
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(verbose_name='Имя категории', max_length=255)

    def __str__(self):
        return self.name


class Ad(TimeStampedModel, HitCountMixin):
    """
    Basic model for ad
    """
    title = models.CharField(verbose_name='Заголовок', max_length=255,
                             db_index=True)
    text = models.TextField(verbose_name="Текст объявления")
    is_active = models.BooleanField(default=True)
    lifetime = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name='Категория',
                                 related_name='categories', blank=True,
                                 null=True)
    owner = models.ForeignKey(AppUser, verbose_name='Владелец',
                              related_name='users', blank=True, null=True)


    def __str__(self):
        return self.title

