# Generated by Django 2.2.16 on 2020-09-09 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_test"),
    ]

    operations = [
        migrations.CreateModel(
            name="NewApp",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user2", models.BigIntegerField()),
            ],
            options={
                "verbose_name_plural": "NewApp",
            },
        ),
    ]
