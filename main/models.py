from django.db import models
from django.conf import settings
# Create your models here.

class hotel_details(models.Model):
    location = models.CharField(max_length=50)
    hotel_image = models.CharField(max_length=150)
    hotel_name = models.CharField(max_length=50)
    hotel_type = models.CharField(max_length=50, default='hotel')
    price = models.IntegerField()
    def __str__(self):
        return str(self.location)+" "+str(self.hotel_image)+" "+str(self.hotel_name)+" "+str(self.price)