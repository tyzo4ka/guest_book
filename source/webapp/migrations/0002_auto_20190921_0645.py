# Generated by Django 2.2.5 on 2019-09-21 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='Unknown', max_length=40, verbose_name='Имя автора')),
                ('email', models.EmailField(max_length=254, verbose_name='почта')),
                ('text', models.TextField(max_length=3000, verbose_name='Текст')),
                ('status', models.CharField(blank=True, choices=[('active', 'Активно'), ('blocked', 'Заблокировано')], default='active', max_length=30, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
