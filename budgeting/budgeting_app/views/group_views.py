from django.shortcuts import render
from django.views import generic
from ..models import Budget_Group
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect


# Create your views here.
class Group_Detail_View(generic.DetailView):
    model = Budget_Group
    template_name = "budgeting_app/group_categories/group_details.html"


class All_Groups_View(generic.ListView):
    template_name = "budgeting_app/group_categories/all_groups.html"
    context_object_name = "all_groups"

    def get_queryset(self):
        return Budget_Group.objects.all()


class Group_Create_View(generic.base.TemplateView):
    template_name = "budgeting_app/group_categories/create_group.html"


def create_group(request):
    created_group = Budget_Group.objects.create(
        group_code=request.POST["group_code"],
        group_name=request.POST["group_name"],
        group_description=request.POST["group_description"],
    )
    return HttpResponseRedirect(
        reverse("budgeting_app:group_detail", args=(created_group.id,))
    )


def edit_group(request, pk):
    budget_group = Budget_Group.objects.get(id=pk)
    budget_group.group_code = request.POST["group_code"]
    budget_group.group_name = request.POST["group_name"]
    budget_group.group_description = request.POST["group_description"]
    budget_group.save()
    return HttpResponseRedirect(
        reverse("budgeting_app:group_detail", args=(budget_group.id,))
    )


def delete_group(request, pk):
    budget_group = Budget_Group.objects.get(id=pk)
    budget_group.delete()
    return HttpResponseRedirect(reverse("budgeting_app:all_groups"))
