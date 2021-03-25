from rest_framework import serializers
from .models import Theme
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers



       
class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'




