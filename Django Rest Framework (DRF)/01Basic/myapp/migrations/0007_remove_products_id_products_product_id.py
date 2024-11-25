# Generated by Django 5.1.3 on 2024-11-23 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='id',
        ),
        migrations.AddField(
            model_name='products',
            name='product_id',
            field=models.CharField(blank=True, max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]
