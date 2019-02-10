# Generated by Django 2.1.2 on 2019-01-17 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20190117_1403'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product',
            new_name='sizeprod',
        ),
        migrations.AddField(
            model_name='sizeprod',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='smoll_l',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='smoll_m',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='smoll_s',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
