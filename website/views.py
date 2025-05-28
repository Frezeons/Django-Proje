from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product

@login_required
def urun_listesi(request):
    urunler = Product.objects.select_related('depo').all()
    return render(request, 'urun_listesi.html', {'urunler': urunler})
