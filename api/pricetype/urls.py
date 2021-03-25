from django.urls import include, path
from .views import PricetypeDetailView, PricetypeListingsView

urlpatterns= [
    path('pricetypelist/', PricetypeListingsView.as_view()),
    path('pricetypedetail/<slug:pk>/', PricetypeDetailView.as_view()),
]