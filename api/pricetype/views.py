from django.shortcuts import render
from rest_framework import generics, permissions, status
from .models import Pricetype
from .serializers import PricetypeSerializer
from .permissions import IsAdminOrReadOnly

class PricetypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pricetype.objects.all()
    serializer_class = PricetypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    lookup_field = 'pk'

class PricetypeListingsView(generics.ListCreateAPIView):
    queryset = Pricetype.objects.all()
    serializer_class = PricetypeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

