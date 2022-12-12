from django import forms
from extra_views import InlineFormSetFactory

from dummydata.models import FakeSchema, FakeSchemaColumn, DataSet


class FakeSchemaForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Write name of schema"})
    )

    class Meta:
        model = FakeSchema
        fields = "__all__"
        widgets = {"author": forms.HiddenInput()}


class FakeCSVSchemaColumnForm(forms.ModelForm):
    column_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Write column name"}),
    )

    class Meta:
        model = FakeSchemaColumn
        fields = "__all__"


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
