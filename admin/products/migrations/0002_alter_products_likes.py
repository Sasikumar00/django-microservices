# Generated by Django 4.2.13 on 2024-06-27 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]