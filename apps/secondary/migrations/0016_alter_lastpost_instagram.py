# Generated by Django 5.0.1 on 2024-01-05 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0015_lastpost_instagram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lastpost',
            name='instagram',
            field=models.ImageField(upload_to='instagram_image/', verbose_name='instagram URL'),
        ),
    ]
