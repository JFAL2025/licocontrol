from django.urls import path
from . import views

urlpatterns = [
    path('', views.panel, name='panel'),
    path('registro_v/', views.registro_v, name='registro_v'),
    path('inventario/', views.inventario, name='inventario'),
    path('reporte/', views.reporte, name='reporte'),
    path('catalogo/', views.catalogo, name='catalogo'),

]
