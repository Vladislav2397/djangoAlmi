# Generated by Django 3.0.5 on 2020-04-28 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20200428_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='subcategory',
            field=models.ManyToManyField(blank=True, related_name='_category_subcategory_+', to='catalog.Category', verbose_name='Подкатегории'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Category', verbose_name='Категория'),
        ),
    ]