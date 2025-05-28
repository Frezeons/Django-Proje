from django.urls import path
from . import views
from .views import urun_listesi

urlpatterns = [
    path('urunler/', views.urun_listesi, name='urun_listesi'),
    path('urunler/sil/<int:pk>/', views.urun_sil, name='urun_sil'),
]
