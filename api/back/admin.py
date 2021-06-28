from django.contrib import admin
from .models import Theme
from mptt.admin import MPTTModelAdmin

class ThemeAdmin(admin.ModelAdmin):
    list_display = ['id']

admin.site.register(Theme, ThemeAdmin)
