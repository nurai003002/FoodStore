# Generated by Django 5.0.1 on 2024-01-09 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0041_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cart',
        ),
    ]