from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('produk/', views.daftar_produk),
    path('produk/<int:id>/', views.detail_produk),
    path('kontak/', views.kontak),
]