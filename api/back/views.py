from rest_framework import generics
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from .models import Theme
from .serializers import ThemeSerializer
from .permissions import IsAdminOrReadOnly
 

class ThemeListView(ListAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    permission_classes = (IsAdminOrReadOnly )



