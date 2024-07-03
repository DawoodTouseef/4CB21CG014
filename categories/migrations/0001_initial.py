# Generated by Django 5.0.6 on 2024-07-03 07:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=520, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoris',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5852, unique=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.companies')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.TextField(max_length=25630)),
                ('price', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('availability', models.BooleanField()),
                ('categoris', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.categoris')),
            ],
        ),
    ]
