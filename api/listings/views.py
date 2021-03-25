from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .permissions import IsAuthorOrReadOnly
from .models import Listing
from categorys.models import Category
from .serializers import ListingSerializer, ListingDetailSerializer, ListingImageSerializer
from django.shortcuts import render, get_object_or_404
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import render

from rest_framework.permissions import AllowAny
from django.shortcuts import render, get_object_or_404


from categorys.models import Category



class ListingListView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Listing.objects.all()
    filter_backends= [SearchFilter, OrderingFilter]
    serializer_class = ListingSerializer
    permission_classes = ( )

class ListingCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Listing.objects.all()
    serializer_class = ListingDetailSerializer
    permission_classes = ( )
    parser_classes = ( MultiPartParser, FormParser)

class ListingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingDetailSerializer
    permission_classes = (IsAuthorOrReadOnly, )

def listing(request, pk, slug):
    listing = get_object_or_404(Listing, id=id)
    if slug != listing.get_slug():
        return redirect(listing)

