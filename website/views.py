from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product

@login_required
def urun_listesi(request):
    urunler = Product.objects.select_related('depo').all()
    return render(request, 'urun_listesi.html', {'urunler': urunler})

@login_required
def urun_sil(request, pk):
    urun = get_object_or_404(Product, pk=pk)
    urun.delete()
    return redirect('urun_listesi')
