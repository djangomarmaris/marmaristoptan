# Generated by Django 4.0.5 on 2022-09-21 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(default='Ürün Kodu Giriniz', max_length=200),
        ),
    ]
