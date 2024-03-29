from django.contrib import admin
from .models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'maximum_speed', 'acquired_date')


admin.site.register(Car, CarAdmin)
