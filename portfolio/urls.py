from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<str:category_name>/', views.category, name='category'),
    path('project/<str:project_name>/', views.project_detail, name='project_detail'),

    # Game demo pages
    path('demo/<str:demo_slug>/', views.game_demo, name='game_demo'),
]