# Generated by Django 4.1.4 on 2023-06-29 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Transaction",
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
                ("amount", models.IntegerField()),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "category",
                    models.IntegerField(
                        choices=[
                            (0, "Food"),
                            (1, "Transports"),
                            (2, "Entertainments"),
                            (3, "Groceries"),
                            (4, "Utilities"),
                            (5, "Other"),
                        ]
                    ),
                ),
                (
                    "transaction_type",
                    models.IntegerField(choices=[(0, "Expense"), (1, "Income")]),
                ),
            ],
        ),
    ]
