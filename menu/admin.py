from django.contrib import admin
from .models import Produk, kategori
# Register your models here.
class ProdukKategori(admin.ModelAdmin):
    list_display = ("Nama", "harga")

admin.site.register(Produk, ProdukKategori)
admin.site.register(kategori)