from django.contrib import admin
from .models import Pin, SoldPin


@admin.register(Pin, SoldPin)
class ViewAdmin(admin.ModelAdmin):
    pass
