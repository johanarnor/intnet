from django.contrib import admin
from activities.models import Price, Activity, CarouselImage, Feature, FeatureOption, DescriptionImage

# Register your models here.

admin.site.register(Price)
admin.site.register(Activity)
admin.site.register(CarouselImage)
admin.site.register(Feature)
admin.site.register(FeatureOption)
admin.site.register(DescriptionImage)