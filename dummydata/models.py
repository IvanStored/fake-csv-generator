from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class FakeSchema(models.Model):

    DELIMITERS = [
        (",", "Comma(,)"),
        (";", "Semilicon(;)"),
        ("\t", "Tab(\t)"),
        (" ", "Space( )"),
        ("|", "Pipe(|)"),
    ]

    QUOTES = [
        ('"', 'Double-quote(")'),
        ("'", "Single-quote(')"),
    ]

    title = models.CharField(
        max_length=63, blank=True, null=True, default="Untitled"
    )
    column_separator = models.TextField(
        choices=DELIMITERS, default=",", max_length=1
    )
    string_character = models.TextField(
        choices=QUOTES, default='""', max_length=1
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="schemas"
    )

    def get_absolute_url(self):
        return reverse("dummydata:schema-detail", kwargs={"pk": self.id})

    class Meta:
        ordering = ["-updated"]


class FakeSchemaColumn(models.Model):

    DATA_TYPES = [
        (0, "Full name (a combination of first name and last name)"),
        (1, "Job"),
        (2, "Email"),
        (3, "Domain name"),
        (4, "Phone number"),
        (5, "Company name"),
        (6, "Text (with a specified range for a number of sentences)"),
        (7, "Integer (with specified range)"),
        (8, "Address"),
        (9, "Date"),
    ]

    column_name = models.CharField(max_length=20)
    data_type = models.IntegerField(choices=DATA_TYPES, default=0)
    order = models.PositiveIntegerField(default=0)
    range_from = models.PositiveIntegerField(default=0, blank=True, null=True)
    range_to = models.PositiveIntegerField(default=0, blank=True, null=True)
    schema = models.ForeignKey(
        FakeSchema, on_delete=models.CASCADE, related_name="schemacolumns"
    )

    class Meta:
        ordering = ["order"]

    def clean(self):
        super(FakeSchemaColumn, self).clean()
        if self.range_from is None or self.range_to is None:
            raise ValidationError({"__all__": "Must be int"})
        if self.range_from > self.range_to:
            raise ValidationError({"__all__": "Min must be less than max."})


class DataSet(models.Model):
    STATUSES = [(0, "Processing.."), (1, "Ready!")]
    schema = models.ForeignKey(
        FakeSchema, on_delete=models.CASCADE, related_name="schemadatasets"
    )
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUSES, default=0)
    rows = models.PositiveIntegerField(null=True)
    download_link = models.URLField()

    class Meta:
        ordering = ["-created"]
