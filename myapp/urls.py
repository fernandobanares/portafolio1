from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),
    path('proyectos/', views.lista_proyectos, name='proyectos'),
]
