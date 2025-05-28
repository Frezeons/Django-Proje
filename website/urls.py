from django.urls import path
from . import views
from .views import urun_listesi

urlpatterns = [
    path('urunler/', urun_listesi, name='urun_listesi'),

]
