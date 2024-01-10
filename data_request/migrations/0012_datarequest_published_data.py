# Generated by Django 4.1.7 on 2023-12-22 07:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("data_catalogue", "0008_remove_datacataloguemeta_data_request"),
        ("data_request", "0011_datarequest_agency"),
    ]

    operations = [
        migrations.AddField(
            model_name="datarequest",
            name="published_data",
            field=models.ManyToManyField(
                blank=True, null=True, to="data_catalogue.datacataloguemeta"
            ),
        ),
    ]
