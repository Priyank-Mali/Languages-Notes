# Generated by Django 5.0.6 on 2024-10-01 06:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('mobile_id', models.CharField(blank=True, max_length=20, primary_key=True, serialize=False)),
                ('model_name', models.CharField(max_length=50)),
                ('price', models.FloatField(blank=True, default=0.0)),
                ('description', models.TextField(blank=True)),
                ('brand_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.brand')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
