import json
import os
import sys
import json
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crud.settings')
django.setup()

from barang.models import Kategori, Status, Produk

# Load JSON data from file
script_directory = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(script_directory, 'data.json')

with open(json_file_path, 'r') as file:
    json_data = json.load(file)

# Function to handle foreign keys
def get_or_create_model(model_class, data):
    instance, created = model_class.objects.get_or_create(**data)
    return instance

# Iterate through JSON data and create database entries
for entry in json_data:
    # Get or create Kategori instance
    kategori_data = {'nama_kategori': entry['kategori']}
    kategori_instance = get_or_create_model(Kategori, kategori_data)

    # Get or create Status instance
    status_data = {'nama_status': entry['status']}
    status_instance = get_or_create_model(Status, status_data)

    # Create Produk instance
    produk_data = {
      'nama_produk': entry['nama_produk'],
      'harga': entry['harga'],
      'id_status': status_instance,
      'id_kategori': kategori_instance
    }
    Produk.objects.create(**produk_data)
