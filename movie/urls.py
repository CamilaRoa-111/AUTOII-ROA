# movie/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                # Página principal
    path('about/', views.about, name='about'),        # Página "Acerca de"
    path('statistics/', views.statistics, name='statistics'),  # Página de estadísticas
]