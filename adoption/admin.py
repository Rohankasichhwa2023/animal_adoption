# adoption/admin.py
from django.contrib import admin
from .models import Animal



@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'age','image')
