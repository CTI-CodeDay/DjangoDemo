# Generated by Django 2.1.7 on 2024-06-12 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='summary',
            field=models.TextField(default='this is cool!'),
        ),
    ]
