# Generated by Django 2.1.2 on 2019-01-17 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20190117_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='smoll_l',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='smoll_m',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='smoll_s',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
