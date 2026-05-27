# game/urls.py
from django.urls import path
from .views import PlayGameView
from . import views

urlpatterns = [
    # Al acceder a /play/ cargará la vista de juego
    path('play/', PlayGameView.as_view(), name='play'),
    # path('instrucciones/', views.instrucciones, name='instrucciones'),
]