from django.contrib import admin
from django.urls import path, include
# import django_rq.urls

local_urls = [
    path('api/', include('home_server.api.urls')),
    path('', admin.site.urls),
]

third_party_urls = [
]

urlpatterns = local_urls + third_party_urls
