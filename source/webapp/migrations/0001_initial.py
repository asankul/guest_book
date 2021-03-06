# Generated by Django 2.2 on 2019-09-21 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuestBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('text', models.TextField(max_length=3000, verbose_name='Текст')),
                ('date_of_creation', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_of_edition', models.DateField(auto_now=True, verbose_name='Дата редактирования')),
                ('status', models.CharField(choices=[('active', 'Активная'), ('blocked', 'Заблокировано')], default='active', max_length=200)),
            ],
        ),
    ]
