# Generated by Django 5.0.3 on 2024-04-25 10:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cars", "0003_car_operational_alter_car_maximum_speed"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="slug",
            field=models.SlugField(default=""),
        ),
    ]
