# Generated by Django 2.1.2 on 2019-02-10 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_auto_20190210_1512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basket',
            old_name='image_product',
            new_name='image',
        ),
    ]
