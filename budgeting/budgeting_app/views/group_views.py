from typing import Any
from django.db.models.query import QuerySet
from django.forms import modelformset_factory
from django.shortcuts import render
from django.views import generic

from ..forms import BudgetGroupForm
from ..models import Budget_Group
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect


class All_Groups_View(generic.ListView):
    template_name = "budgeting_app/groups_templates/all_groups.html"
    # adding form
    form_class = BudgetGroupForm
    context_object_name = "all_groups"

    def get_queryset(self) -> QuerySet[Any]:
        return Budget_Group.objects.all().order_by("group_code")

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        BudgetGroupFormSet = modelformset_factory(
            Budget_Group, form=BudgetGroupForm, extra=1
        )
        if self.request.method == "POST":
            formset = BudgetGroupFormSet(request.POST)
            print(formset.errors)
            if formset.is_valid():
                print("Formset valid")
                formset.save()
                return HttpResponseRedirect(reverse("budgeting_app:all_groups"))
        else:
            formset = BudgetGroupFormSet(queryset=Budget_Group.objects.none())
        context["formset"] = formset
        return context

    def post(self, request, *args, **kwargs):
        BudgetGroupFormset = modelformset_factory(
            Budget_Group, form=BudgetGroupForm, extra=1
        )
        if request.method == "POST":
            formset = BudgetGroupFormset(request.POST)
            if formset.is_valid():
                formset.save()
                return HttpResponseRedirect(reverse("budgeting_app:all_groups"))