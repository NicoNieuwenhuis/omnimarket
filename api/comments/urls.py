from django.urls import path, include
from django.contrib import admin

from .views import CommentListAPIView, CommentDetailAPIView, CommentListListingsAPIView

urlpatterns = [
    path('comments/', CommentListAPIView.as_view(), name='list'),
    path('comments/<int:pk>/', CommentDetailAPIView.as_view(), name='thread'),
    path('commentslistings/<slug:listing_slug>-<int:listing_id>/', CommentListListingsAPIView.as_view(), name='listing'),
]