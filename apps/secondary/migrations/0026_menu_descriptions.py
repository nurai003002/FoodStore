# Generated by Django 5.0.1 on 2024-01-07 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0025_rename_bi_category_category_big_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='descriptions',
            field=models.TextField(default=1, verbose_name='Описание'),
            preserve_default=False,
        ),
    ]
