# Generated by Django 5.0.3 on 2024-04-25 10:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cars", "0004_car_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="slug",
            field=models.SlugField(blank=True, default=""),
        ),
    ]
