# Generated by Django 2.1.7 on 2023-06-21 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20230621_0451'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(null=True),
        ),
    ]
