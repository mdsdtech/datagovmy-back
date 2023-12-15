# Generated by Django 4.1.7 on 2023-12-04 07:23

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DataRequest",
            fields=[
                (
                    "ticket_id",
                    models.AutoField(editable=False, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                (
                    "institution",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("dataset_title", models.CharField(max_length=255)),
                ("dataset_title_en", models.CharField(max_length=255, null=True)),
                ("dataset_title_ms", models.CharField(max_length=255, null=True)),
                ("dataset_description", models.TextField()),
                ("dataset_description_en", models.TextField(null=True)),
                ("dataset_description_ms", models.TextField(null=True)),
                ("agency", models.CharField(max_length=255)),
                ("purpose_of_request", models.CharField(max_length=255)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("submitted", "Submitted"),
                            ("under_review", "Under Review"),
                            ("rejected", "Rejected"),
                            ("in_progress", "In Progress"),
                            ("data_published", "Data Published"),
                        ],
                        default="submitted",
                        max_length=20,
                    ),
                ),
            ],
        ),
    ]