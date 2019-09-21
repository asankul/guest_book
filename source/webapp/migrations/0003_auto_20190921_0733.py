# Generated by Django 2.2 on 2019-09-21 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20190921_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestbook',
            name='date_of_creation',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='guestbook',
            name='date_of_edition',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Дата редактирования'),
        ),
    ]