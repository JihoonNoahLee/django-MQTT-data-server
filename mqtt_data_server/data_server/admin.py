from django.contrib import admin
from .models import Data
# Register your models here.

@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'date', 
        'temperature', 
        'humidity', 
    )
