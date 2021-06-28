from django.shortcuts import render
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics, permissions
from .models import Category
from listings.models import Listing
from listings.serializers import ListingSerializer
from .serializers import CategoriesSerializer
from .permissions import IsAdminOrReadOnly
from django.db import connection
from rest_framework.decorators import api_view
from django.db import connection, connections, transaction, DEFAULT_DB_ALIAS
from django.shortcuts import render, get_object_or_404

import mysql.connector
import pymysql as MySQLdb



class CategoryListingsView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        cat_id = self.kwargs.get('pk', None)
        if cat_id is not None:
            category = get_object_or_404(Category, id=cat_id)
            return Listing.objects.filter(category__in=Category.objects.get(pk=cat_id).get_descendants(include_self=True))
        else:
            return Listing.objects.none()

class CategorieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

class CategorieListingsView(generics.ListCreateAPIView):
    queryset = Category.objects.filter(parent=None)
    serializer_class = CategoriesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


#class CreatecategorieView(generics.ListCreateAPIView):
#
#    def post(self, request):
#        serializer = CategoriesSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#    mydb = mysql.connector.connect(
#  	host="localhost",
#  	user="root",
#  	password="642#Denhaag",
#  	database="estuaries1",
#  	auth_plugin='mysql_native_password' )
#    mycursor = mydb.cursor()
#    mycursor.execute("CREATE TABLE dfsrn ( name VARCHAR(255), address VARCHAR(255))")
    






