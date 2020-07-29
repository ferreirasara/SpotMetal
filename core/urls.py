from django.urls import path
from .views import index, dashboard, settings, results, aboutUs, saveToFile

urlpatterns = [
    path('', index, name='index'),
    path('dashboard', dashboard, name='dashboard'),
    path('settings', settings, name='settings'),
    path('results', results, name='results'),
    path('about-us', aboutUs, name='aboutUs'),
    path('save-to-file', saveToFile, name='saveToFile'),
]
