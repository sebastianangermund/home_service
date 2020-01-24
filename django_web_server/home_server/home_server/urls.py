from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


local_urls = [
    path('api/', include('home_server.api.urls')),
    path('', admin.site.urls),
]

urlpatterns = local_urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
