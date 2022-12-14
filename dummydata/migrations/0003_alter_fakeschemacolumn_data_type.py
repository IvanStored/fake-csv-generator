# Generated by Django 4.1.4 on 2022-12-12 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dummydata", "0002_alter_fakeschemacolumn_data_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fakeschemacolumn",
            name="data_type",
            field=models.CharField(
                choices=[
                    (
                        "Full_name",
                        "Full name (a combination of first name and last name)",
                    ),
                    ("Job", "Job"),
                    ("Email", "Email"),
                    ("Domain", "Domain name"),
                    ("Phone", "Phone number"),
                    ("Company", "Company name"),
                    ("Text", "Text (with a specified range for a number of sentences)"),
                    ("Integer", "Integer (with specified range)"),
                    ("Address", "Address"),
                    ("Date", "Date"),
                ],
                default="Full_name",
                max_length=20,
            ),
        ),
    ]
