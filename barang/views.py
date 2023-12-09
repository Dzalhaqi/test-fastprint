from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from .models import Produk, Kategori, Status
from .forms import ProdukForm

def index(request):
  produk_list = Produk.objects.filter(
    id_status__nama_status='bisa dijual').select_related('id_status').order_by('id_produk')

  return render(request, 'barang/index.html', {
    'produk_list': produk_list
  })


def edit(request, id):
    produk = get_object_or_404(Produk, id_produk=id)

    if request.method == 'POST':
        initial_data = {
            'id_kategori': produk.id_kategori,
            'nama_produk': produk.nama_produk,
            'id_status': produk.id_status,
            'harga': produk.harga
        }

        form = ProdukForm(request.POST, initial=initial_data)

        if request.POST.get('edit'):
          form = ProdukForm(initial=initial_data)
          return render(request, 'barang/edit.html', {'form': form, 'produk': produk})

        if form.is_valid():
            produk.nama_produk = form.cleaned_data['nama_produk']
            produk.harga = form.cleaned_data['harga']
            produk.id_status = form.cleaned_data['id_status']
            produk.id_kategori = form.cleaned_data['id_kategori']
            produk.save()

            return redirect('barang:index')
        
        return render(request, 'barang/edit.html', {'form': form, 'produk': produk})
    else:
        return redirect('barang:index')



def tambah(request):
    if request.method == 'POST':
        form = ProdukForm(request.POST)
        if form.is_valid():
            nama_produk = form.cleaned_data['nama_produk']
            harga = form.cleaned_data['harga']
            id_status = form.cleaned_data['id_status']
            id_kategori = form.cleaned_data['id_kategori']

            produk = Produk(
                nama_produk=nama_produk,
                harga=harga,
                id_status=id_status,
                id_kategori=id_kategori
            )
            produk.save()

            return redirect('barang:index')
    else:
        form = ProdukForm()

    return render(request, 'barang/tambah.html', {'form': form})


def hapus(request, id):
  produk = get_object_or_404(Produk, id_produk=id)

  if request.method == 'DELETE':
      # produk.delete()
      return JsonResponse({'message': 'Produk berhasil dihapus.'}, status=200)

  return render(request, 'barang/hapus.html', {'produk': produk})
