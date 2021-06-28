from rest_framework import serializers
from .models import Pricetype

class PricetypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricetype
        fields = "__all__"