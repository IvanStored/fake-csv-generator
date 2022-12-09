from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin
from extra_views import CreateWithInlinesView, UpdateWithInlinesView
from .generator import generate_csv_file

from dummydata.forms import (
    FakeSchemaForm,
    FakeCSVSchemaColumnInline,
    DataSetForm,
)
from dummydata.models import FakeSchema, DataSet


class Login(LoginView):
    template_name = "registration/login.html"
    redirect_authenticated_user = True


class FakeSchemaListView(LoginRequiredMixin, generic.ListView):
    model = FakeSchema
    queryset = FakeSchema.objects.all()
    paginate_by = 5
    template_name = "dummydata/schemalist.html"

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)


class FakeSchemaCreate(LoginRequiredMixin, CreateWithInlinesView):
    model = FakeSchema
    form_class = FakeSchemaForm
    inlines = [
        FakeCSVSchemaColumnInline,
    ]
    template_name = "dummydata/schema-form.html"

    def get_initial(self):
        return {"author": self.request.user}

    def get_success_url(self):
        if "action" in self.request.POST:
            if self.request.POST["action"] == "add_column":
                return reverse_lazy(
                    "dummydata:schema-edit", kwargs={"pk": self.object.pk}
                )
            elif self.request.POST["action"] == "submit":
                return reverse_lazy("dummydata:schema-list")
        return reverse_lazy("dummydata:schema-list")


class FakeSchemaEdit(
    LoginRequiredMixin, UserPassesTestMixin, UpdateWithInlinesView
):
    model = FakeSchema
    form_class = FakeSchemaForm
    inlines = [
        FakeCSVSchemaColumnInline,
    ]
    template_name = "dummydata/schema-form.html"

    def get_success_url(self):
        if "action" in self.request.POST:
            if self.request.POST["action"] == "add_column":
                return reverse_lazy(
                    "dummydata:schema-edit", kwargs={"pk": self.object.pk}
                )
            elif self.request.POST["action"] == "submit":
                return reverse_lazy("dummydata:schema-list")
        return reverse_lazy("dummydata:schema-list")

    def test_func(self):
        schema = self.get_object()
        return schema.author == self.request.user


@login_required
def delete(request, pk):
    schema = FakeSchema.objects.get(pk=pk)
    if schema.author == request.user:
        schema.delete()
        return HttpResponseRedirect(reverse_lazy("dummydata:schema-list"))
    return HttpResponseRedirect(reverse_lazy("dummydata:schema-list"))


class DataSetsView(
    LoginRequiredMixin, UserPassesTestMixin, FormMixin, generic.DetailView
):
    model = FakeSchema
    form_class = DataSetForm
    template_name = "dummydata/datasets.html"

    def test_func(self):
        schema = self.get_object()
        return schema.author == self.request.user

    def post(self, request, *args, **kwargs):
        schema = self.get_object()
        dataset = DataSet.objects.create(
            schema=schema, rows=int(request.POST["rows"])
        )
        dataset.download_link = generate_csv_file(dataset)
        dataset.status = 1
        dataset.save()
        return HttpResponseRedirect(
            reverse_lazy(
                "dummydata:schema-detail", kwargs={"pk": schema.pk}
            )
        )
