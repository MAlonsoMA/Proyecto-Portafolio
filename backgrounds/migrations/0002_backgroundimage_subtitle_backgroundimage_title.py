# Generated by Django 4.2.8 on 2024-06-06 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backgrounds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='backgroundimage',
            name='subtitle',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='subtitular'),
        ),
        migrations.AddField(
            model_name='backgroundimage',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='titular'),
        ),
    ]