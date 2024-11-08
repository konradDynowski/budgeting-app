from typing import Any
from django.forms import modelformset_factory
from django.shortcuts import render
from django.views import generic

from ..forms import BudgetCategoryForm
from ..models import Budget_Group, Budget_Category
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect


class All_Categories_View(generic.ListView):
    template_name = "budgeting_app/category_templates/all_categories.html"
    form_class = BudgetCategoryForm
    context_object_name = "all_categories"

    def get_queryset(self):
        return Budget_Category.objects.all().order_by("group_id", "id")

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        BudgetCategoryFormSet = modelformset_factory(
            Budget_Category, form=BudgetCategoryForm, extra=1
        )
        if self.request.method == "POST":
            formset = BudgetCategoryFormSet(self.request.POST)
            print(formset.errors)
            if formset.is_valid():
                print("formset valid")
                formset.save()
                return HttpResponseRedirect(reverse("budgeting_app:all_categories"))
        else:
            formset = BudgetCategoryFormSet(queryset=Budget_Category.objects.none())
        context["formset"] = formset
        return context

    def post(self, request, *args, **kwargs):
        BudgetCategoryFormset = modelformset_factory(
            Budget_Category, form=BudgetCategoryForm, extra=1
        )
        if request.method == "POST":
            formset = BudgetCategoryFormset(request.POST)
            if formset.is_valid():
                formset.save()
                return HttpResponseRedirect(reverse("budgeting_app:all_categories"))
