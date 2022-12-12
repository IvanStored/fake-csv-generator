# Fake CSV Generator

Check it out -> [Let`s try!](ivanstored.pythonanywhere.com)

admin

1qazcde3


## Features

- Any user can log in to the system with a username and password.
- Any logged-in user can create any number of data schemas to create
datasets with fake data.
- Each such data schema has a name and a list of columns with names and
specified data types.
- Users can build the data schema with any number of columns of any type
described above. Some types support extra arguments (like a range),
while others do not.
- Each column also has its own name (which will be a column header in the
CSV file) and order (just a number to manage column order).

# Technology Stack:

- Python 3.10
- Django
- MDBootstrap

# Local installation

```sh
git clone https://github.com/IvanStored/fake-csv-generator
cd fake-csv-generator
python -m venv venv
venv/scripts/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver  # starts Django project
```
