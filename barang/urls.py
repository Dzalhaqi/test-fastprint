from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = 'barang'

urlpatterns = [
  path('', index, name='index'),
  path('tambah', tambah, name='tambah'),
  path('edit/<int:id>', edit, name='edit'),
  path('hapus/<int:id>', hapus, name='hapus') 
] 