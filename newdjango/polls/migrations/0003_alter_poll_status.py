# Generated by Django 5.1 on 2024-08-22 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0002_alter_poll_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="poll",
            name="status",
            field=models.BooleanField(db_index=True, verbose_name="Active"),
        ),
    ]
