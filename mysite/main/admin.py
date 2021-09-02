from django.contrib import admin
from .models import Tutorial, TutorialSeries, TutorialCategory, Asset
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

class AssetAdmin(admin.ModelAdmin):

    fied_sets = [("Location/Date", {"fields": ["asset_location", "asset_published"]}),
                 ("URL", {'fields': ["asset_slug"]}),
                 ("Rent", {'fields': ["asset_rent"]}),
                 ("Tenant", {'fields': ["asset_tenant"]}),
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols':80, 'rows':30})},
    }

admin.site.register(Asset, AssetAdmin)
