# Generated by Django 5.0.1 on 2024-01-09 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0035_rename_comments_review_comment_news_comments'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
