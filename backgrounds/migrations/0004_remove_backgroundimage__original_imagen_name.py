# Generated by Django 4.2.8 on 2024-06-06 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backgrounds', '0003_backgroundimage__original_imagen_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backgroundimage',
            name='_original_imagen_name',
        ),
    ]
