# Generated by Django 4.0.5 on 2022-09-18 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_alter_slider_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='up',
            field=models.CharField(choices=[('Bal Çeşitleri', 'Bal Çeşitleri'), ('Arı Ürünleri', 'Arı Ürünleri'), ('Reçel & Pekmez', 'Reçel & Pekmez'), ('Yöresel Ürünler', 'Yöresel Ürünler'), ('Zeytin & Zeytinyağı', 'Zeytin & Zeytinyağı'), ('Sağlık Ürünleri', 'Sağlık Ürünleri'), ('Badem Ürünleri', 'Badem Ürünleri')], default='Ürün Üst Modeli Nedir?', max_length=100),
        ),
    ]