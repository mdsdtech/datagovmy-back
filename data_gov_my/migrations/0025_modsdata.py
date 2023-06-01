# Generated by Django 4.1.7 on 2023-05-18 08:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("data_gov_my", "0024_alter_catalogjson_catalog_data_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ModsData",
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
                ("expertise_area", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                ("institution", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=500)),
            ],
        ),
    ]