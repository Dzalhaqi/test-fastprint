# Generated by Django 4.2 on 2023-12-09 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id_kategori', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID Kategori')),
                ('nama_kategori', models.CharField(help_text='Masukkan kategori', max_length=255, verbose_name='Nama Kategori')),
            ],
            options={
                'verbose_name': 'Kategori',
                'verbose_name_plural': 'Kategori',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id_status', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID Status')),
                ('nama_status', models.CharField(help_text='Masukkan nama status', max_length=255, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Status',
            },
        ),
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id_produk', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID Produk')),
                ('nama_produk', models.CharField(help_text='Masukkan nama produk', max_length=255, verbose_name='Nama Produk')),
                ('harga', models.FloatField(help_text='Masukkan harga', verbose_name='Harga')),
                ('id_kategori', models.ForeignKey(db_column='id_kategori', on_delete=django.db.models.deletion.CASCADE, related_name='produk_kategori', related_query_name='produk', to='barang.kategori')),
                ('id_status', models.ForeignKey(db_column='id_status', on_delete=django.db.models.deletion.CASCADE, related_name='produk_status', related_query_name='produk', to='barang.status')),
            ],
            options={
                'verbose_name': 'Produk',
                'verbose_name_plural': 'Produk',
            },
        ),
    ]
