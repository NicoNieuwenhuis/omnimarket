from rest_framework import serializers
from listings.models import Listing, ListingImage
from rest_framework.serializers import SerializerMethodField
from rest_framework.fields import IntegerField

from sorl.thumbnail import get_thumbnail

class ListingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingImage
        fields = "__all__"

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'  

class ListingDetailSerializer(serializers.ModelSerializer):
    images = ListingImageSerializer(many=True, required=False, read_only=True)
  
    class Meta:
        model = Listing
        fields =  ('__all__' )  


    def create(self, validated_data):
        images_data = self.context['request'].FILES
        listing = Listing.objects.create(
            name=validated_data.get('name'), 
            category=validated_data.get('category'), 
            pricetype=validated_data.get('pricetype'), 
            firstimage=validated_data.get('firstimage'), 
            hasprice=validated_data.get('hasprice'),
            )
        for image_data in images_data.getlist('images'):
            ListingImage.objects.create(listing=listing, image=image_data)
        return listing       

