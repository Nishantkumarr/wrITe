# Generated by Django 3.0.6 on 2020-06-03 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200601_0433'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default='location', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='user_website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
