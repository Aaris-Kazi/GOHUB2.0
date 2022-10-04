from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class Hotel(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['location', 'hotel_name', 'hotel_type', 'price']
    ordering= ['location']

admin.site.register(models.hotel_details, Hotel)

class Booking(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['userid', 'hotelid', 'location', 'startday', 'endday', 'price']
    ordering= ['id']

admin.site.register(models.hotel_booking, Booking)