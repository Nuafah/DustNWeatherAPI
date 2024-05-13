from django.urls import include, path
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register(r'weather', views.WeatherViewSet)
router.register(r'dust', views.DustViewSet)
router.register(r'dustnweather', views.DustNWeatherViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.index, name='index'),
    path('<str:location>/', views.detail, name="detail"),
]