# Generated by Django 2.1.7 on 2025-01-16 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='summary',
            field=models.TextField(),
        ),
    ]
