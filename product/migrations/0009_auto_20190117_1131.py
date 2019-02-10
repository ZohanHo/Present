# Generated by Django 2.1.2 on 2019-01-17 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_sizeprod_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='sizeprod',
            name='kg',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sizeprod',
            name='product',
            field=models.ManyToManyField(related_name='size', to='product.Product'),
        ),
    ]