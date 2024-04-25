import logging

from django.contrib import admin

from .models import Car

logger = logging.getLogger(__name__)


class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'operational', 'maximum_speed', 'acquired_date')
    prepopulated_fields = {"slug": ['name', 'acquired_date']}

    def save_model(self, request, obj, form, change):
        logger.debug(f"name: {obj.name}, acquired_date: {obj.acquired_date}")
        super().save_model(request, obj, form, change)


admin.site.register(Car, CarAdmin)
