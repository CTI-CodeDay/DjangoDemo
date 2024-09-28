# Generated by Django 5.1.1 on 2024-09-28 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_alter_product_description_alter_product_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="featured",
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="product",
            name="summary",
            field=models.TextField(),
        ),
    ]
