# Generated by Django 5.1.3 on 2024-11-23 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_productcategory_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='product_id',
            field=models.CharField(blank=True, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]