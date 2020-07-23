from django.urls import path
from .views import index, dashboard, settings

urlpatterns = [
    path('', index, name='index'),
    path('dashboard', dashboard, name='dashboard'),
    path('settings', settings, name='settings'),
]
