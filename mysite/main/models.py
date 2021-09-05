from django.db import models
from datetime import datetime



class People(models.Model):
    Owner = models.BooleanField()
    people_name = models.CharField(max_length=200)
    people_surname = models.CharField(max_length=200)
    people_phone_number = models.CharField(max_length=200)
    people_email = models.EmailField(max_length=254)
    people_occupation = models.CharField(max_length=200)
    people_revenue = models.IntegerField()
    people_slug = models.CharField(max_length=200, default=1)

    def __str__(self):
        return self.people_name

class Asset(models.Model):
    asset_location = models.CharField(max_length=200)
    asset_size = models.CharField(max_length=200)
    asset_price = models.FloatField()
    asset_rent = models.FloatField()
    asset_slug = models.CharField(max_length=200, default=1)
    asset_published = models.DateTimeField('date published', default=datetime.now())
    asset_tenant = models.ForeignKey(People, related_name="tenant_asset", on_delete=models.CASCADE, limit_choices_to={'Owner': False})
    asset_owner = models.ForeignKey(People, related_name="assets", on_delete=models.CASCADE, limit_choices_to={'Owner': True})

    class Meta:
        order_with_respect_to = 'asset_owner'

    def __str__(self):
        return self.asset_location

class Finances(models.Model):
    pass