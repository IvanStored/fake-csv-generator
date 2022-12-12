from django.urls import path

from .views import (
    FakeSchemaListView,
    FakeSchemaCreate,
    FakeSchemaEdit,
    DataSetsView,
    Login,
    SchemaDelete,
)

urlpatterns = [
    path("", Login.as_view(), name="index"),
    path("schemas/", FakeSchemaListView.as_view(), name="schema-list"),
    path("schemas/create/", FakeSchemaCreate.as_view(), name="schema-create"),
    path(
        "schemas/edit/<int:pk>/", FakeSchemaEdit.as_view(), name="schema-edit"
    ),
    path(
        "schemas/delete/<int:pk>/",
        SchemaDelete.as_view(),
        name="schema-delete",
    ),
    path("schemas/<int:pk>/", DataSetsView.as_view(), name="schema-detail"),
]
app_name = "dummydata"
