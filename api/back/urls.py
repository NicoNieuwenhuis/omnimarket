from django.urls import path
from back.views import ThemeListView

urlpatterns = [
    path('themelist/', ThemeListView.as_view()),
]