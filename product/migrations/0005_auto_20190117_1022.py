# Generated by Django 2.1.2 on 2019-01-17 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20190117_0949'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productsize',
            options={'verbose_name': 'Размер товара', 'verbose_name_plural': 'Размер товаров'},
        ),
    ]
