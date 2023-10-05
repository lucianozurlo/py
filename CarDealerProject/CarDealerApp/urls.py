from django.urls import path
from CarDealerApp import views

urlpatterns = [
    path('', views.buscarFlota, name="Home"),
    path('flota/', views.flota, name="Flota"),
    path('choferes/', views.choferes, name="Choferes"),
    path('puntosDeRetiro/', views.puntosDeRetiro, name="PuntosDeRetiro"),
    path('cargarFlota/', views.cargarFlota, name="CargarFlota"),
    path('cargarChofer/', views.cargarChofer, name="CargarChofer"),
    path('cargarPuntoDeRetiro/', views.cargarPuntoDeRetiro, name="CargarPuntoDeRetiro")]

