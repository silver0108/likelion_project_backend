# Generated by Django 4.0.4 on 2022-06-21 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]