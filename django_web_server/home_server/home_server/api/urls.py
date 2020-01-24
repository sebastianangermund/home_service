from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'photos', views.PhotoViewSet)

user_urls = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

auth_urls = [
    path('api-auth/', include('rest_framework.urls')),
]

led_urls = [
    path('lights/ledlights/', views.LedLightList.as_view(),
         name='led-list-all'),
    path('lights/ledlights/<uuid:pk>/', views.LedLightDetail.as_view(),
         name='led-detail'),
    path('lights/ledlights/<uuid:pk>/state/', views.LedLightState.as_view(),
         name='led-state'),
]

photo_urls = [
    path(r'', include(router.urls)),
]

service_urls = [
    path('service/write-data-points/', views.write_data_points),
]

urlpatterns = user_urls + auth_urls + led_urls + photo_urls + service_urls
