# Generated by Django 3.0.5 on 2020-04-29 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20200428_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='category',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Category', verbose_name='Подкатегории'),
        ),
    ]
