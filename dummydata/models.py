from django.contrib.auth import get_user_model
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

    title = models.CharField(max_length=63, blank=True, null=True)
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
        ("Full_name", "Full name (a combination of first name and last name)"),
        ("Job", "Job"),
        ("Email", "Email"),
        ("Domain", "Domain name"),
        ("Phone", "Phone number"),
        ("Company", "Company name"),
        ("Text", "Text (with a specified range for a number of sentences)"),
        ("Integer", "Integer (with specified range)"),
        ("Address", "Address"),
        ("Date", "Date"),
    ]

    column_name = models.CharField(max_length=20)
    data_type = models.CharField(max_length=20, choices=DATA_TYPES)
    order = models.PositiveIntegerField(default=0)
    schema = models.ForeignKey(
        FakeSchema, on_delete=models.CASCADE, related_name="schemacolumns"
    )

    class Meta:
        ordering = ["order"]

    def clean(self):
        super(FakeSchemaColumn, self).clean()
        if not self.order:
            self.order = (
                FakeSchemaColumn.objects.filter(schema=self.schema).count() + 1
            )


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
