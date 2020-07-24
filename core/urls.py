from django.urls import path
from .views import index, dashboard, settings, search, results, aboutUs

urlpatterns = [
    path('', index, name='index'),
    path('search', search, name='search'),
    path('dashboard', dashboard, name='dashboard'),
    path('settings', settings, name='settings'),
    path('results', results, name='results'),
    path('about-us', aboutUs, name='aboutUs'),
]
