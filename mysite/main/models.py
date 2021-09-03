from django.db import models
from datetime import datetime

CHOICES = (('TENANT', 'Tenant'), ('LANDLORD', 'Landlord'))

class Asset(models.Model):
    asset_location = models.CharField(max_length=200)
    asset_size = models.CharField(max_length=200)
    asset_price = models.FloatField()
    asset_rent = models.FloatField()
    asset_slug = models.CharField(max_length=200, default=1)
    asset_published = models.DateTimeField('date published', default=datetime.now())

    def __str__(self):
        return self.asset_location

class People(models.Model):
    people_type = models.CharField(max_length=200, choices=CHOICES, default='Tenant')
    people_name = models.CharField(max_length=200)
    people_surname = models.CharField(max_length=200)
    people_phone_number = models.CharField(max_length=200)
    people_email = models.EmailField(max_length=254)
    people_occupation = models.CharField(max_length=200)
    people_revenue = models.FloatField()
    people_asset = models.ForeignKey(Asset, default=1, verbose_name="Asset", on_delete=models.SET_DEFAULT)
    people_slug = models.CharField(max_length=200, default=1)

    def __str__(self):
        return self.people_name





































