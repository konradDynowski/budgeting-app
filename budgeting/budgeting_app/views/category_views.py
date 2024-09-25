from typing import Any
from django.shortcuts import render
from django.views import generic
from ..models import Budget_Group, Budget_Category
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect


# Create your views here.
class Category_Detail_View(generic.DetailView):
    model = Budget_Category
    template_name = "budgeting_app/category_templates/category_details.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["groups"] = Budget_Group.objects.all()

        return context


class All_Categories_View(generic.ListView):
    template_name = "budgeting_app/category_templates/all_categories.html"
    context_object_name = "all_categories"

    def get_queryset(self):
        return Budget_Category.objects.all()


class Category_Create_View(generic.base.TemplateView):
    template_name = "budgeting_app/category_templates/create_category.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["groups"] = Budget_Group.objects.all()
        return context


def create_category(request):
    created_category = Budget_Category.objects.create(
        group_id=Budget_Group.objects.get(pk=request.POST["group_id"]),
        category_code=request.POST["category_code"],
        category_name=request.POST["category_name"],
        category_description=request.POST["category_description"],
    )
    return HttpResponseRedirect(
        reverse("budgeting_app:category_detail", args=(created_category.id,))
    )


def edit_category(request, pk):
    budget_category = Budget_Category.objects.get(id=pk)
    budget_category.category_code = request.POST["category_code"]
    budget_category.category_name = request.POST["category_name"]
    budget_category.category_description = request.POST["category_description"]
    budget_category.group_id = Budget_Group.objects.get(pk=request.POST["group_id"])
    budget_category.save()
    return HttpResponseRedirect(
        reverse("budgeting_app:category_detail", args=(budget_category.id,))
    )


def delete_category(request, pk):
    budget_category = Budget_Category.objects.get(id=pk)
    budget_category.delete()
    return HttpResponseRedirect(reverse("budgeting_app:all_categories"))
