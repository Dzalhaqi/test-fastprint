from tabnanny import verbose
from django.db import models

class Kategori(models.Model):
  id_kategori = models.BigAutoField(
    verbose_name='ID Kategori',
    primary_key=True)
  nama_kategori = models.CharField(
    verbose_name='Nama Kategori',
    help_text='Masukkan kategori',
    max_length=255)
  
  class Meta: 
    verbose_name = "Kategori"
    verbose_name_plural = "Kategori"

  def __str__(self):
        return self.nama_kategori

class Status(models.Model):
  id_status = models.BigAutoField(
    verbose_name='ID Status',
    primary_key=True)
  nama_status = models.CharField(
    verbose_name='Status',
    help_text='Masukkan nama status',
    max_length=255)
  
  class Meta: 
    verbose_name = "Status"
    verbose_name_plural = "Status"

  def __str__(self):
        return self.nama_status

class Produk(models.Model):
  id_produk = models.BigAutoField(
    verbose_name='ID Produk',
    primary_key=True)
  nama_produk = models.CharField(
    verbose_name='Nama Produk',
    help_text='Masukkan nama produk',
    max_length=255)
  harga = models.FloatField(
    verbose_name='Harga',
    help_text='Masukkan harga')
  id_status = models.ForeignKey(
    to='Status',
    on_delete=models.CASCADE,
    related_name='produk_status',
    related_query_name='produk',
    db_column='id_status')
  id_kategori = models.ForeignKey(
    to='Kategori',
    on_delete=models.CASCADE,
    related_name='produk_kategori',
    related_query_name='produk',
    db_column='id_kategori')
  
  class Meta: 
        verbose_name = 'Produk'
        verbose_name_plural = "Produk"

