from django.db import models
from datetime import datetime

class People(models.Model):
    OWNER = 'owner'
    TENANT = 'tenant'
    TYPES = ((OWNER, 'Owner'), (TENANT, 'Tenant'))
    type = models.CharField(max_length=15, blank=True, choices=TYPES)
    people_name = models.CharField(max_length=200)
    people_surname = models.CharField(max_length=200)
    people_phone_number = models.CharField(max_length=200)
    people_email = models.EmailField(max_length=254)
    people_occupation = models.CharField(max_length=200)
    people_revenue = models.IntegerField()
    people_slug = models.CharField(max_length=200, default=1)

    def __str__(self):
        return self.people_name

class Tenant(models.Model):
    tenants = People.objects.filter(type=People.TYPES[1])

class Owner(models.Model):
    owners = People.objects.filter(type=People.TYPES[0])

class Asset(models.Model):
    asset_location = models.CharField(max_length=200)
    asset_size = models.CharField(max_length=200)
    asset_price = models.FloatField()
    asset_rent = models.FloatField()
    asset_slug = models.CharField(max_length=200, default=1)
    asset_published = models.DateTimeField('date published', default=datetime.now())
    asset_tenant = models.OneToOneField(Tenant, related_name="tenant", on_delete=models.CASCADE)
    asset_owner = models.OneToOneField(Owner, related_name="owner", on_delete=models.CASCADE)

    def __str__(self):
        return self.asset_location


