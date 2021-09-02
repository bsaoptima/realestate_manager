from django.db import models
from datetime import datetime

class TutorialCategory(models.Model):
    '''
    Since Categories will have multiple attributes (images, links, etc), we make a new class
    '''

    tutorial_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200, default=1) #category link

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.tutorial_category

class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=200)

    tutorial_category = models.ForeignKey(TutorialCategory,
                                          default=1,
                                          verbose_name="Category",
                                          on_delete=models.SET_DEFAULT) #If category gets deleted, tutorial have their category set to defaults

    series_summary = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Series"

    def __str__(self):
        return self.tutorial_series

class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField('date published', default=datetime.now())
    #https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.ForeignKey.on_delete
    tutorial_series = models.ForeignKey(TutorialSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
    tutorial_slug = models.CharField(max_length=200, default=1)

    def __str__(self):
        return self.tutorial_title

class Asset(models.Model):
    asset_location = models.CharField(max_length=200)
    asset_size = models.CharField(max_length=200)
    asset_price = models.CharField(max_length=200)
    asset_rent = models.CharField(max_length=200)
    asset_tenant = models.ForeignKey(Tenants, default=1, verbose_name="Tenant", on_delete=models.SET_DEFAULT)
    asset_slug= models.CharField(max_length=200, default=1)
    asset_published = models.DateTimeField('date published', default=datetime.now())

    def __str__(self):
        return self.asset_location