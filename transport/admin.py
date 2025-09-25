from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.html import format_html
from .models import Route, Bus, Registration

class BusAdmin(admin.ModelAdmin):
    list_display = ('number','route','capacity','time_slot','driver_preview')
    readonly_fields = ('driver_preview',)

    def driver_preview(self, obj):
        if obj.driver_photo:
            return format_html('<img src="{}" width="100" height="100"/>', obj.driver_photo.url)
        return "(No photo)"

admin.site.register(Route)
admin.site.register(Bus, BusAdmin)
admin.site.register(Registration)
