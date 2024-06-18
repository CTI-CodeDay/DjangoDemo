# Generated by Django 5.0.6 on 2024-06-18 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_description_alter_product_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='summary',
            field=models.TextField(default='This is cool!'),
        ),
    ]
