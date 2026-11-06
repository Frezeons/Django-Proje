# Django-Proje

> Depolara bağlı ürünlerin listelenip eklendiği ve silindiği basit bir envanter yönetim sistemi.

**Durum:** arşiv · **Stack:** Python · Django 5.2 · django-unfold (admin teması) · SQLite · Gunicorn

## Ne yapar
- Depo (`Depo`: ad, adres) ve ürün (`Product`: ad, adet, açıklama, eklenme tarihi) modelleri; her ürün bir depoya bağlı
- Ürün listeleme, ekleme ve silme (`/urunler/`, `/urunler/ekle/`, `/urunler/sil/<id>/`)
- django-unfold ile modernleştirilmiş admin paneli
- Ayrı `login` uygulaması

## Dizin yapısı
```
inventory_system/  # proje ayarları
website/           # Depo/Product modelleri, ürün view'ları
login/             # giriş uygulaması
manage.py
requirements.txt
```

## Çalıştırma
```bash
python -m venv venv && venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver   # http://127.0.0.1:8000/urunler/
```

## Notlar
- `db.sqlite3` repoya dahil edilmiş durumda.
