# Generated by Django 2.1.2 on 2019-02-10 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0023_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='buket',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=True, to='product.CategoryProduct'),
        ),
    ]
