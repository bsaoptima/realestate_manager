from django.contrib import admin
from .models import Asset, People, Tenant, Owner
from tinymce.widgets import TinyMCE
from django.db import models

#Register your models here.

class PeopleAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Type", {"fields": ["type"]}),
        ("Information", {"fields": ["people_name",
                                    "people_surname",
                                    "people_phone_number",
                                    "people_email",
                                    "people_occupation",
                                    "people_revenue"]}),
        ("URL", {"fields": ["people_slug"]}),
    ]

    list_filter = ("type",)

class AssetAdmin(admin.ModelAdmin):

    fieldsets = [("Location/Date", {"fields": ["asset_location", "asset_published"]}),
                 ("URL", {"fields": ["asset_slug"]}),
                 ("Rent", {"fields": ["asset_rent"]}),
                 ("Tenant", {"fields": ["asset_tenant"]}),
    ]

class OwnerAdmin(admin.ModelAdmin):
    list_display = ("owners",)


admin.site.register(People, PeopleAdmin)
admin.site.register(Tenant, PeopleAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Asset, AssetAdmin)
