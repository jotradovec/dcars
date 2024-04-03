from django.contrib import admin
from .models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'operational', 'maximum_speed', 'acquired_date')


admin.site.register(Car, CarAdmin)
