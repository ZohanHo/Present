# Generated by Django 2.1.2 on 2019-01-17 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_delete_productsize'),
    ]

    operations = [
        migrations.AddField(
            model_name='sizeprod',
            name='product',
            field=models.ManyToManyField(to='product.Product'),
        ),
    ]
