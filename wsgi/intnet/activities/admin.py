from django.contrib import admin
from activities.models import Price, Activity, Feature, FeatureOption

# Register your models here.

admin.site.register(Price)
admin.site.register(Activity)
admin.site.register(Feature)
admin.site.register(FeatureOption)