# Generated by Django 3.0.5 on 2020-04-29 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20200429_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='isPackage',
            field=models.BooleanField(default=False, verbose_name='Пакет категорий'),
        ),
    ]