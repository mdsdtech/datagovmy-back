# Generated by Django 4.1.7 on 2023-12-22 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("data_request", "0010_remove_datarequest_agency"),
    ]

    operations = [
        migrations.AddField(
            model_name="datarequest",
            name="agency",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="data_request.agency",
            ),
        ),
    ]