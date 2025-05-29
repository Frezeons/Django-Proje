from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Product
from .forms import ProductForm

@login_required
def urun_listesi(request):
    urunler = Product.objects.select_related('depo').all()
    return render(request, 'urun_listesi.html', {'urunler': urunler})

@login_required
def urun_sil(request, pk):
    urun = get_object_or_404(Product, pk=pk)
    urun.delete()
    return redirect('urun_listesi')

@login_required
def urun_ekle(request):
    if not request.user.is_superuser:
        messages.error(request, "Bu işlemi yapmak için yetkiniz yok.")
        return redirect('home')  # URL adı neyse onu yaz

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ürün başarıyla eklendi.")
            return redirect('urun_listesi')
    else:
        form = ProductForm()
    return render(request, 'urun_ekle.html', {'form': form})