# Generated by Django 4.0.5 on 2022-09-18 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_slider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%y/%m/%d'),
        ),
    ]
