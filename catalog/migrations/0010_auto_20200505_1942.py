# Generated by Django 3.0.5 on 2020-05-05 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_category_ispackage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='isTop',
            field=models.BooleanField(default=False, verbose_name='Это хит продаж'),
        ),
        migrations.AddField(
            model_name='product',
            name='pub_date',
            field=models.DateField(null=True, verbose_name='Дата публикации'),
        ),
    ]
