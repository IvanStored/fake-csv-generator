# Generated by Django 4.1.4 on 2022-12-09 09:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="FakeSchema",
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
                (
                    "title",
                    models.CharField(
                        blank=True, default="Untitled", max_length=63, null=True
                    ),
                ),
                (
                    "column_separator",
                    models.TextField(
                        choices=[
                            (",", "Comma(,)"),
                            (";", "Semilicon(;)"),
                            ("\t", "Tab(\t)"),
                            (" ", "Space( )"),
                            ("|", "Pipe(|)"),
                        ],
                        default=",",
                        max_length=1,
                    ),
                ),
                (
                    "string_character",
                    models.TextField(
                        choices=[('"', 'Double-quote(")'), ("'", "Single-quote(')")],
                        default='""',
                        max_length=1,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="schemas",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-updated"],
            },
        ),
        migrations.CreateModel(
            name="FakeSchemaColumn",
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
                ("column_name", models.CharField(max_length=20)),
                (
                    "data_type",
                    models.IntegerField(
                        choices=[
                            (
                                0,
                                "Full name (a combination of first name and last name)",
                            ),
                            (1, "Job"),
                            (2, "Email"),
                            (3, "Domain name"),
                            (4, "Phone number"),
                            (5, "Company name"),
                            (
                                6,
                                "Text (with a specified range for a number of sentences)",
                            ),
                            (7, "Integer (with specified range)"),
                            (8, "Address"),
                            (9, "Date"),
                        ],
                        default=0,
                    ),
                ),
                ("order", models.PositiveIntegerField(default=0)),
                (
                    "range_from",
                    models.PositiveIntegerField(blank=True, default=0, null=True),
                ),
                (
                    "range_to",
                    models.PositiveIntegerField(blank=True, default=0, null=True),
                ),
                (
                    "schema",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="schemacolumns",
                        to="dummydata.fakeschema",
                    ),
                ),
            ],
            options={
                "ordering": ["order"],
            },
        ),
        migrations.CreateModel(
            name="DataSet",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Processing.."), (1, "Ready!")], default=0
                    ),
                ),
                ("rows", models.PositiveIntegerField(null=True)),
                ("download_link", models.URLField()),
                (
                    "schema",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="schemadatasets",
                        to="dummydata.fakeschema",
                    ),
                ),
            ],
            options={
                "ordering": ["-created"],
            },
        ),
    ]
