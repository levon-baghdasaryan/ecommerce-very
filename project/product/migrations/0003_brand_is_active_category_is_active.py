# Generated by Django 4.2.6 on 2023-10-29 17:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0002_alter_productline_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="brand",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="category",
            name="is_active",
            field=models.BooleanField(default=False),
        ),
    ]
