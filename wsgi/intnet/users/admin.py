from django.contrib import admin
from users.models import DirrUser, PCode, City
# Register your models here.

admin.site.register(DirrUser)
admin.site.register(PCode)
admin.site.register(City)