from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.html import format_html
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','role','university_id','photo_preview')
    readonly_fields = ('photo_preview',)

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="100" height="100"/>', obj.photo.url)
        return "(No photo)"

admin.site.register(User, UserAdmin)
