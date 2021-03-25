from django.urls import path, include
from .views import *
from django.urls import path
from listings import views
from rest_framework.routers import DefaultRouter
#router = DefaultRouter()
#router.register(r'', ListingViewSet)

from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 

from comments.views import CommentListListingsAPIView


urlpatterns = [
    path('listings/', ListingListView.as_view()),
	path('listings/<slug:slug>-<int:pk>/', ListingDetailView.as_view()),
	path('listings/<slug:listing_slug>-<int:listing_id>/comments/', CommentListListingsAPIView.as_view()),
	path('create-listing/', ListingCreateView.as_view(), name='create-listing'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
