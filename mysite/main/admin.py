from django.contrib import admin
from .models import Asset, People
from tinymce.widgets import TinyMCE
from django.db import models

#Register your models here.

'''
class TutorialAdmin(admin.ModelAdmin):

    field_sets = [("Title/Date", {"fields": ["tutorial_title", "tutorial_published"]}),
                  ("URL", {'fields': ["tutorial_slug"]}),
                  ("Series", {'fields': ["tutorial_series"]}),
                  ("Content", {"fields": ["tutorial_content"]}),
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols':80, 'rows': 30})},
    }

#admin.site.register(TutorialSeries)
#admin.site.register(TutorialCategory)
#admin.site.register(Tutorial, TutorialAdmin)
    '''
class PeopleAdmin(admin.ModelAdmin):

    field_sets = [("Name/Surname", {"fields": ["people_name", "people_surname"]}),
                  ("URL", {"fields": ["people_slug"]}),
                  ("Occupation", {"fields": ["people_occupation"]}),
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }

class AssetAdmin(admin.ModelAdmin):

    fied_sets = [("Location/Date", {"fields": ["asset_location", "asset_published"]}),
                 ("URL", {"fields": ["asset_slug"]}),
                 ("Rent", {"fields": ["asset_rent"]}),
                 ("Tenant", {"fields": ["asset_tenant"]}),
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols':80, 'rows':30})},
    }

admin.site.register(People, PeopleAdmin)
admin.site.register(Asset, AssetAdmin)
