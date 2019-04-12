from django.urls import path
from django.conf.urls import include
from . import views

user_urls = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

auth_urls = [
    path('api-auth/', include('rest_framework.urls')),
]

led_urls = [
    path('things/ledlights/', views.LedLightList.as_view(),
         name='led-list-all'),
    path('things/ledlights/<uuid:pk>/', views.LedLightDetail.as_view(),
         name='led-detail'),
    path('things/ledlights/<uuid:pk>/state/', views.LedLightState.as_view(),
         name='led-state'),
]

service_urls = [
    path('service/management-commands/', views.ManagementConnands.as_view(),
         name='management-commands')
]

urlpatterns = user_urls + auth_urls + led_urls + service_urls
