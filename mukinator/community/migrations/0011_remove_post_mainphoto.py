# Generated by Django 4.0.4 on 2022-06-22 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0010_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='mainphoto',
        ),
    ]