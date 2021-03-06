# Generated by Django 3.0.5 on 2020-04-29 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20200429_1151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='category',
            name='isMain',
            field=models.BooleanField(default=False, verbose_name='Главная категория'),
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Category', verbose_name='Родитель'),
        ),
    ]
