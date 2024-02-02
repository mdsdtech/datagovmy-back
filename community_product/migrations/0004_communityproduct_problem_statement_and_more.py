# Generated by Django 4.2.6 on 2024-02-02 08:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("community_product", "0003_alter_communityproduct_product_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="communityproduct",
            name="problem_statement",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="communityproduct",
            name="solutions_developed",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
    ]
