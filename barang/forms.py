from django import forms
from .models import Produk, Kategori, Status

class ProdukForm(forms.Form):
    nama_produk = forms.CharField(label='Nama Produk', required=False)
    harga = forms.DecimalField(label='Harga', decimal_places=3, required=False)
    id_status = forms.ModelChoiceField(queryset=Status.objects.all(), label='Status', required=False)
    id_kategori = forms.ModelChoiceField(queryset=Kategori.objects.all(), label='Kategori', required=False)
    kategori_baru = forms.CharField(label='Kategori Baru', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        existing_categories = Kategori.objects.all()
        self.fields['id_kategori'].queryset = existing_categories

        choices = [(obj.id_kategori, obj.nama_kategori) for obj in existing_categories]
        choices += [('', 'Buat Kategori Baru')]
        self.fields['id_kategori'].choices = choices

    
    def clean(self):
        cleaned_data = super().clean()
        nama_produk = cleaned_data.get('nama_produk')
        harga = cleaned_data.get('harga')
        id_status = cleaned_data.get('id_status')
        id_kategori = cleaned_data.get('id_kategori')
        kategori_baru_user = cleaned_data.get('kategori_baru')

        if not nama_produk:
            self.add_error('nama_produk', forms.ValidationError("Nama produk harus diisi"))

        if not id_status:
            self.add_error('id_status', forms.ValidationError('Status harus diisi'))

        if not harga:
            self.add_error('harga', forms.ValidationError('Harga harus diisi dan dengan angka'))

        if not id_kategori and not kategori_baru_user:
            self.add_error('kategori_baru', forms.ValidationError('Isi bagian ini jika memilih Buat Kategori Baru'))
        elif id_kategori and kategori_baru_user:
            self.add_error('kategori_baru', forms.ValidationError('Jangan isi bagian ini jika tidak memilih Buat Kategori Baru'))

        if id_kategori is None and kategori_baru_user:
            kategori_baru_user = kategori_baru_user.upper().strip()
            if not kategori_baru_user:
                self.add_error('kategori_baru', forms.ValidationError('Nama Kategori tidak boleh kosong'))
            else:
                print(kategori_baru_user)
                created_kategori_baru, _ = Kategori.objects.get_or_create(nama_kategori=kategori_baru_user)
                cleaned_data['id_kategori'] = created_kategori_baru
                del cleaned_data['kategori_baru']

        return cleaned_data