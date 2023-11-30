# Generated by Django 4.2.7 on 2023-11-29 12:48

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FoodTruck",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("location_id", models.CharField(max_length=100, unique=True)),
                ("applicant", models.CharField(max_length=200)),
                ("facility_type", models.CharField(max_length=100)),
                ("cnn", models.CharField(max_length=100)),
                ("location_description", models.CharField(max_length=300)),
                ("address", models.CharField(max_length=200)),
                ("blocklot", models.CharField(max_length=100)),
                ("block", models.CharField(max_length=50)),
                ("lot", models.CharField(max_length=50)),
                ("permit", models.CharField(max_length=100)),
                ("status", models.CharField(max_length=100)),
                ("food_items", models.TextField()),
                ("x", models.FloatField()),
                ("y", models.FloatField()),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                ("schedule_url", models.URLField()),
                ("dayshours", models.CharField(blank=True, max_length=100, null=True)),
                ("noi_sent", models.DateTimeField(blank=True, null=True)),
                ("approved", models.DateTimeField(blank=True, null=True)),
                ("received", models.DateTimeField(blank=True, null=True)),
                ("prior_permit", models.IntegerField()),
                ("expiration_date", models.DateTimeField()),
                (
                    "fire_prevention_districts",
                    models.IntegerField(blank=True, null=True),
                ),
                ("police_districts", models.IntegerField(blank=True, null=True)),
                ("supervisor_districts", models.IntegerField(blank=True, null=True)),
                ("zip_codes", models.IntegerField(blank=True, null=True)),
                (
                    "neighborhoods",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
            ],
        ),
    ]
