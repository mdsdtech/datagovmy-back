# Generated by Django 4.1.7 on 2024-04-30 06:50

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("data_gov_my", "0077_delete_viewcount"),
    ]

    operations = [
        migrations.CreateModel(
            name="PublicationSubscription",
            fields=[
                (
                    "publication_type",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                (
                    "emails",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.EmailField(max_length=254),
                        default=list,
                        size=None,
                    ),
                ),
            ],
        ),
    ]