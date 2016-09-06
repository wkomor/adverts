from django.contrib import admin
from .models import Ad, Category


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    """
    Ad administration
    """
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Category administration
    """
    pass
