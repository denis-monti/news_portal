# Generated by Django 4.1.4 on 2023-02-09 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_output', '0017_alter_likedislike_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='likedislike',
            options={'ordering': ['-news__published'], 'verbose_name': 'Лайки и дизлайки', 'verbose_name_plural': 'Список лайков'},
        ),
    ]
