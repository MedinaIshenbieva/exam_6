# Generated by Django 4.0.1 on 2022-01-08 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuestBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200, verbose_name='Автор')),
                ('email', models.EmailField(max_length=200, verbose_name='Имейл')),
                ('text', models.TextField(max_length=2000, verbose_name='Текст записи')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата изменения')),
                ('status', models.CharField(choices=[('active', 'Активно'), ('blocked', 'Заблокировано')], default='active', verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Гостевая книга',
                'db_table': 'guest_book',
            },
        ),
    ]
