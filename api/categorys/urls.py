from django.urls import path
from .views import CategorieListingsView, CategoryListingsView, CategorieDetailView
from django.urls import include, path
from django.conf.urls import url

urlpatterns= [
    path('categorieslist/', CategorieListingsView.as_view()),
    path('categorydetail/<slug:slug>-<int:pk>/', CategorieDetailView.as_view(), name='categoriedetail'),
    path('categorylistings/<slug:slug>-<int:pk>/', CategoryListingsView.as_view(), name='categorie'),

]

#urlpatterns = [
#    path('catcreatetab/', createtab),
#]