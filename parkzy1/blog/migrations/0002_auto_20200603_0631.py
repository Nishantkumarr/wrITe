# Generated by Django 3.0.6 on 2020-06-03 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='book_author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='book_writer',
            field=models.CharField(default='name of writer', max_length=180),
        ),
        migrations.AlterField(
            model_name='post',
            name='book_name',
            field=models.CharField(default='name of book', max_length=180),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=180),
        ),
    ]
