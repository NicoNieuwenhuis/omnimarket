from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics, permissions
from .models import Comment
from listings.models import Listing
from django.shortcuts import render, get_object_or_404
from .serializers import CommentSerializer, CommentDetailSerializer
from .permissions import IsAuthorOrReadOnly



class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    lookup_field = 'pk'
    #lookup_url_kwarg = "abc"
    permission_classes = (IsAuthorOrReadOnly, )


class CommentListAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends= [SearchFilter, OrderingFilter]
    search_fields = ['content', 'user__first_name']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    


class CommentListListingsAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Comment.objects.all()
    lookup_field = 'id'

    def get_queryset(self, *args, **kwargs):
        listing_id = self.kwargs.get('listing_id', 'listing_slug')
        return Comment.objects.filter(listing=listing_id)