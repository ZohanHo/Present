# Generated by Django 2.1.2 on 2019-02-10 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0024_auto_20190210_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=True, to='product.CategoryProduct'),
        ),
        migrations.AddField(
            model_name='chocolate',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=True, to='product.CategoryProduct'),
        ),
    ]
