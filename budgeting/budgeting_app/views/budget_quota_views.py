from typing import Any
from django.views import generic
from ..forms import GenerateQuotasForMonthForm
from ..models import Category_Quota, Budget_Category, Budget_Group, Budget_Transaction
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from datetime import date
import calendar as cal
from django.db.models import QuerySet
import numpy as np


class GenerateBudgetView(generic.FormView):
    template_name = "budgeting_app/budgeting_quota/generate_for_month.html"
    form_class = GenerateQuotasForMonthForm

    def form_valid(self, form):
        month = int(form.cleaned_data["month"])
        year = int(form.cleaned_data["year"])

        generate_budgeting_quotas(month, year)
        return HttpResponseRedirect(
            reverse(
                "budgeting_app:month_planning",
                kwargs={"date_month": str(month) + "-" + str(year)},
            )
        )


class PlanMonthView(generic.ListView):
    template_name = "budgeting_app/budgeting_quota/plan_month.html"
    context_object_name = "quotas_for_month"
    year = 0
    month = 0

    def get_queryset(self) -> QuerySet[Any]:
        dm = self.kwargs.get("date_month")
        self.year = int(dm.split("-")[1])
        self.month = int(dm.split("-")[0])
        self.refdate = date(self.year, self.month, 1)

        queryset = Category_Quota.objects.filter(quota_date__exact=self.refdate)
        return queryset

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:

        context = super().get_context_data(**kwargs)

        max_date = date(
            self.year, self.month, cal.monthrange(self.year, self.refdate.month)[1]
        )

        txn_cat_grp_dict = {
            group: {
                "categories": {
                    category: {
                        "txns": Budget_Transaction.objects.filter(
                            transaction_date__lte=max_date,
                            transaction_date__gte=self.refdate,
                            category_id__exact=category,
                            active_flag__exact=True,
                        )
                    }
                    for category in Budget_Category.objects.filter(
                        active_flag__exact=True, group_id__exact=group
                    )
                }
            }
            for group in Budget_Group.objects.filter(active_flag__exact=True)
        }

        for group in txn_cat_grp_dict:
            groupsum = 0
            groupplansum = 0
            for category in txn_cat_grp_dict[group]["categories"]:
                category_sum = 0
                for transaction in txn_cat_grp_dict[group]["categories"][category][
                    "txns"
                ]:
                    category_sum += transaction.transaction_amount
                txn_cat_grp_dict[group]["categories"][category][
                    "category_sum"
                ] = category_sum
                txn_cat_grp_dict[group]["categories"][category][
                    "quota"
                ] = self.get_queryset().get(category_id=category)
                groupplansum += (
                    self.get_queryset().get(category_id=category).planned_amount
                )
                groupsum += category_sum

            txn_cat_grp_dict[group]["group_sum"] = groupsum
            txn_cat_grp_dict[group]["group_quota"] = groupplansum

        context["txn_cat_grp_dict"] = txn_cat_grp_dict
        return context

    def post(self, request, *args, **kwargs):
        form_data = request.POST

        for k, v in form_data.items():
            if k.startswith("category_quota"):
                quota_id = k.split("_")[-1]
                try:
                    my_quota = Category_Quota.objects.get(pk=quota_id)
                    my_quota.planned_amount = float(v)
                    my_quota.save()
                except Category_Quota.DoesNotExist:
                    print("not exist")
                    pass
        return redirect(reverse("budgeting_app:month_planning", kwargs=self.kwargs))


def generate_budgeting_quotas(month, year):
    all_active_categories = Budget_Category.objects.filter(active_flag__exact=True)
    for category in all_active_categories:
        Category_Quota.objects.get_or_create(
            category_id=category,
            quota_date=date(year, month, 1),
        )
        
class Home_Page_View(generic.ListView):
    template_name = "budgeting_app/budgeting_quota/home.html"
    def get_queryset(self):
        return None
