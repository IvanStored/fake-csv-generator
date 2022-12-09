from django.urls import path

from .views import (
    FakeSchemaListView,
    FakeSchemaCreate,
    FakeSchemaEdit,
    delete,
    DataSetsView,
    Login,
)

urlpatterns = [
    path("", Login.as_view(), name="index"),
    path("schemas/", FakeSchemaListView.as_view(), name="schema-list"),
    path("schemas/create", FakeSchemaCreate.as_view(), name="schema-create"),
    path(
        "schemas/edit/<int:pk>", FakeSchemaEdit.as_view(), name="schema-edit"
    ),
    path("schemas/delete/<int:pk>", delete, name="schema-delete"),
    path("schemas/<int:pk>/", DataSetsView.as_view(), name="schema-detail"),
]
app_name = "dummydata"
