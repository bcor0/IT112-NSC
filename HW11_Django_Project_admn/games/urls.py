
from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.get_all_games, name='get_all_games'),
    path('single/', views.get_single_game, name='get_single_game'),
    path('create/', views.create_game, name='create_game'),
]
