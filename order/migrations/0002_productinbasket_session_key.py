# Generated by Django 2.1.2 on 2019-02-18 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinbasket',
            name='session_key',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]