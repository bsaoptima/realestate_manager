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

class Tenant(models.Model):
    people = models.OneToOneField(People, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'Owner': False})

class Owner(models.Model):
    people = models.OneToOneField(People, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'Owner': True})
    cashflow = None


class Asset(models.Model):
    asset_location = models.CharField(max_length=200)
    asset_size = models.CharField(max_length=200)
    asset_price = models.FloatField()
    asset_rent = models.FloatField()
    asset_slug = models.CharField(max_length=200, default=1)
    asset_published = models.DateTimeField('date published', default=datetime.now())

    '''Problems with these lines, django.db.utils.IntegrityError: UNIQUE constraint failed: new__main_asset.asset_owner_id'''
    asset_tenant = models.ForeignKey(Tenant, related_name="tenant", on_delete=models.CASCADE)
    asset_owner = models.ForeignKey(Owner, related_name="owner", on_delete=models.CASCADE)

    def __str__(self):
        return self.asset_location


