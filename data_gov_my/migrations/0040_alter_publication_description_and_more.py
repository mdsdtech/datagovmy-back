# Generated by Django 4.1.7 on 2023-08-07 07:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("data_gov_my", "0039_publication_publicationresource_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="publication",
            name="description",
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name="publicationresource",
            name="resource_type",
            field=models.CharField(max_length=50),
        ),
    ]