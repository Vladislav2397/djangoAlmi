# Generated by Django 3.0.5 on 2020-04-28 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20200428_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(verbose_name='Цена'),
        ),
    ]