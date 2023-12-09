from django.contrib import admin
from .models import Kategori, Produk, Status


@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
  list_display = ('nama_kategori', 'id_kategori') 

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
  list_display = ('nama_status', 'id_status') 

@admin.register(Produk)
class ProdukAdmin(admin.ModelAdmin):
  list_display = ('id_produk', 'nama_produk', 'harga', 'get_produk_status', 'get_produk_kategori')

  def get_produk_status(self, obj):
      return obj.id_status.nama_status  # Replace 'nama_status' with the actual field name in the 'Status' model

  def get_produk_kategori(self, obj):
      return obj.id_kategori.nama_kategori  # Replace 'nama_kategori' with the actual field name in the 'Kategori' model

  get_produk_status.short_description = 'Status'  # Customize the column header
  get_produk_kategori.short_description = 'Kategori'  # Customize the column header
