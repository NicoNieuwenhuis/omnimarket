from django.contrib import admin
from .models import Pricetype
# Register your models here.
@admin.register(Pricetype)
class PricetypeAdmin(admin.ModelAdmin):
 
    class Meta:
       model = Pricetype