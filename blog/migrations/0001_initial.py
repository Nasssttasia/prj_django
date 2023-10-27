# Generated by Django 4.2.5 on 2023-10-24 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='заголовок')),
                ('slug', models.CharField(max_length=200, verbose_name='slug')),
                ('body', models.TextField(verbose_name='содержимое')),
                ('img', models.ImageField(blank=True, null=True, upload_to='blog_img/', verbose_name='изображение')),
                ('date', models.DateField(verbose_name='дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('views_count', models.IntegerField(default=0, verbose_name='просмотры')),
            ],
            options={
                'verbose_name': 'запись в блоге',
                'verbose_name_plural': 'записи в блоге',
            },
        ),
    ]