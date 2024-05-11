from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='index/')),
    path('index/', views.index),
    path('index/<int:id>', views.detail),
]
