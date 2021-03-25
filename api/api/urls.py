from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

import debug_toolbar


urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path("api/rest-auth/", include('authrest.urls')),
    path('api/', include('users.urls')),
    path('api/', include('listings.urls')),
    path("api/", include('back.urls')),
    path("api/", include('comments.urls')),
    path("api/", include('categorys.urls')),
    path("api/", include('pricetype.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)