# Generated by Django 4.2.5 on 2023-10-05 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='')),
                ('description', models.CharField(max_length=300, verbose_name='')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='')),
                ('price', models.IntegerField()),
                ('date_of_creation', models.DateField()),
                ('date_of_change', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
                'ordering': ('title',),
            },
        ),
    ]