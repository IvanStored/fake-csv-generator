from django import forms
from extra_views import InlineFormSetFactory

from dummydata.models import FakeSchema, FakeSchemaColumn, DataSet


class FakeSchemaForm(forms.ModelForm):
    class Meta:
        model = FakeSchema
        fields = "__all__"
        widgets = {"author": forms.HiddenInput()}


class FakeCSVSchemaColumnForm(forms.ModelForm):
    class Meta:
        model = FakeSchemaColumn
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(),
            "order": forms.NumberInput(),
            "data_type": forms.Select(),
            "data_range_from": forms.NumberInput(),
            "data_range_to": forms.NumberInput(),
        }


class FakeCSVSchemaColumnInline(InlineFormSetFactory):
    model = FakeSchemaColumn
    form_class = FakeCSVSchemaColumnForm
    fields = "__all__"

    factory_kwargs = {
        "extra": 1,
        "max_num": None,
        "can_order": False,
        "can_delete": True,
    }


class DataSetForm(forms.ModelForm):
    class Meta:
        model = DataSet
        fields = ("rows",)
