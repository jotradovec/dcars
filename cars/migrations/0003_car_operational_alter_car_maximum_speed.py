# Generated by Django 5.0.3 on 2024-04-03 11:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cars", "0002_car_acquired_date_car_maximum_speed"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="operational",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="car",
            name="maximum_speed",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
