from django.db import models
from datetime import datetime
from realtors.models import Realtor

# This models will be converted into DB table using migrations.
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING) # Realtor is FK
    title = models.CharField(max_length=256)
    adress = models.CharField(max_length=256)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True) # blank = True,Makes this field optional
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/') # inside media folder yearmonthday
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # inside media folder yearmonthday
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # inside media folder yearmonthday
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # inside media folder yearmonthday
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # inside media folder yearmonthday
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # inside media folder yearmonthday
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # inside media folder yearmonthday
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title # Main field to display
   
    
