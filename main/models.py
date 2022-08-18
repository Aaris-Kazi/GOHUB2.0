from django.db import models
from django.conf import settings
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.core.signals import request_finished, request_started
# Create your models here.

class hotel_details(models.Model):
    location = models.CharField(max_length=50)
    hotel_image = models.CharField(max_length=150)
    hotel_name = models.CharField(max_length=50)
    hotel_type = models.CharField(max_length=50, default='hotel')
    price = models.IntegerField()
    def __str__(self):
        return str(self.location)+" "+str(self.hotel_image)+" "+str(self.hotel_name)+" "+str(self.price)

class resultsnotfound(models.Model):
    location = models.CharField(max_length=50)
    def __str__(self):  
        return str(self.location)

# @receiver(request_finished)
@receiver( post_save, sender=hotel_details)
def missingLoctionHandler(sender, instance, created, *args, **kwargs):
    if created:
        print('Hotels and hotelname', instance.location)
    else:
        print(instance.location)
    print(args, kwargs)


# post_save.connect(missingLoctionHandler, sender=hotel_details, receiver=resultsnotfound)
# post_delete.connect(missingLoctionHandler)