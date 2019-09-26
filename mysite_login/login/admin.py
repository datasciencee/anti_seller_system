from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.User)

admin.site.register(models.conventional_field)
admin.site.register(models.reverse_to_sell, blank=True)

