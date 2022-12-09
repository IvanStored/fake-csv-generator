import csv

from django.conf import settings
from faker import Faker

from .models import DataSet, FakeSchema, FakeSchemaColumn


def generate_fake_data(type_: int, range_: tuple[int, int] = (0, 0)) -> str:
    fake = Faker()
    fake_data = {
        0: fake.name(),
        1: fake.job(),
        2: fake.email(),
        3: fake.email().split("@")[-1],
        4: fake.phone_number(),
        5: fake.company(),
        6: fake.sentences(nb=fake.random_int(min=range_[0], max=range_[1])),
        7: fake.random_int(*range_),
        8: fake.address(),
        9: fake.date(),
    }
    return fake_data[type_]


def generate_csv_file(dataset: DataSet) -> str:
    schema = FakeSchema.objects.get(id=dataset.schema.id)
    columns = (
        FakeSchemaColumn.objects.filter(schema=schema)
        .order_by("order")
        .values()
    )

    delimiter = schema.column_separator
    quote = schema.string_character

    csv.register_dialect(
        "custom",
        delimiter=delimiter,
        quotechar=quote,
        quoting=csv.QUOTE_ALL,
    )

    headers = [column["column_name"] for column in columns]

    with open(
        settings.MEDIA_ROOT + f"/schema{schema.title}_dataset{dataset.id}.csv",
        "w",
    ) as file:
        writer = csv.DictWriter(file, fieldnames=headers, dialect="custom")
        writer.writeheader()

        for row in range(dataset.rows):

            row = {}
            for column in columns:
                value = generate_fake_data(column["data_type"])
                if column["data_type"] in (6, 7):
                    value = generate_fake_data(
                        column["data_type"],
                        range_=(column["range_from"], column["range_to"]),
                    )
                row[column["column_name"]] = value

            writer.writerow(row)

    return f"{settings.MEDIA_URL}schema{schema.title}_dataset{dataset.id}.csv"
