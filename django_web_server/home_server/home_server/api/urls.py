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
    path('things/ledlights/<uuid:pk>/status/', views.LedLightOnOff.as_view(),
         name='led-status'),
]

urlpatterns = user_urls + auth_urls + led_urls
