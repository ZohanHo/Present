# Generated by Django 2.1.2 on 2019-01-18 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_auto_20190117_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recording',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rec', models.CharField(max_length=100)),
            ],
        ),
    ]
