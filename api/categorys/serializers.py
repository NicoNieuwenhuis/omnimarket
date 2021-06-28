from rest_framework import serializers
from .models import  Category
from listings.models import  Listing
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_recursive.fields import RecursiveField
from collections import OrderedDict
from operator import itemgetter

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('id', 'slug', 'name', 'price', 'author', 'image', 'category')

class ChildSerializer(serializers.ModelSerializer):
    children = serializers.ListSerializer(read_only=True, child=RecursiveField())

    class Meta:
        model = Category
        fields = ('id', 'slug', 'name', 'parent', 'children', 'pricetype')

class CategoriesSerializer(serializers.ModelSerializer):
    children = ChildSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'parent', 'children', 'pricetype')

