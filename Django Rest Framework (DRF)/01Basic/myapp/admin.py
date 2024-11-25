from django.contrib import admin
from .models import ProductCategory,Products

# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Products)