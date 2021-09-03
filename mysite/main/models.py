from django.db import models
from datetime import datetime

class People(models.Model):
    people_type = models.CharField(max_length=200)
    people_name = models.CharField(max_length=200)
    people_surname = models.CharField(max_length=200)
    people_phone_number = models.CharField(max_length=200)
    people_email = models.CharField(max_length=200)
    people_occupation = models.CharField(max_length=200)
    people_revenue = models.CharField(max_length=200)
    people_slug = models.CharField(max_length=200, default=1)

    def __str__(self):
        return self.people_name, self.people_surname

class Asset(models.Model):
    asset_location = models.CharField(max_length=200)
    asset_size = models.CharField(max_length=200)
    asset_price = models.CharField(max_length=200)
    asset_rent = models.CharField(max_length=200)
    asset_tenant = models.CharField(max_length=200)
    asset_slug = models.CharField(max_length=200, default=1)
    asset_published = models.DateTimeField('date published', default=datetime.now())

    def __str__(self):
        return self.asset_location







































