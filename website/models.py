from django.db import models

class Depo(models.Model):
    ad = models.CharField(max_length=100)
    adres = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'website_depo'  # veritabanındaki tablo adı

    def __str__(self):
        return self.ad


class Product(models.Model):  
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)

    depo = models.ForeignKey('Depo', on_delete=models.CASCADE, related_name='products')

    class Meta:
        db_table = 'website_product'  # veritabanındaki tablo adı

    def __str__(self):
        return f"{self.name} ({self.depo.ad})"
