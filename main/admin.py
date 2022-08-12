from django.contrib import admin
from . import models
# Register your models here.

class Hotel(admin.ModelAdmin):
    list_display = ['location', 'hotel_name', 'hotel_type', 'price']
    ordering= ['location']

admin.site.register(models.hotel_details, Hotel)
