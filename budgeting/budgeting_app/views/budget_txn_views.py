import calendar

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from datetime import date

from ..forms import BudgetTransactionForm, FilterAllTransactions
from django.forms import modelformset_factory
from ..models import Budget_Transaction


class AllTransactionsView(generic.ListView):
    template_name = "budgeting_app/transaction_templates/all_transactions.html"
    form_class = BudgetTransactionForm
    context_object_name = "all_txns"

    def get_queryset(self):
        queryset = Budget_Transaction.objects.all()
        date_from = self.request.GET.get("date_from")
        date_to = self.request.GET.get("date_to")

        if not (date_from and date_to):
            td = date.today()
            date_from = date(td.year, td.month, 1)
            date_to = date(td.year, td.month, calendar.monthrange(td.year, td.month)[1])
        queryset = queryset.filter(
            transaction_date__gte=date_from, transaction_date__lte=date_to
        )
        queryset = queryset.order_by("transaction_date")
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        form = FilterAllTransactions(self.request.GET or None)
        context["form"] = form

        BudgetTransactionFormSet = modelformset_factory(
            Budget_Transaction, form=BudgetTransactionForm, extra=1
        )
        if self.request.method == "POST":
            formset = BudgetTransactionFormSet(request.POST)
            print(formset.errors)
            if formset.is_valid():
                print("formset is valid")
                formset.save()
                return HttpResponseRedirect(reverse("budgeting_app:all_transactions"))
        else:
            formset = BudgetTransactionFormSet(
                queryset=Budget_Transaction.objects.none()
            )

        context["formset"] = formset
        return context

    def post(self, request, *args, **kwargs):
        BudgetTransactionFormset = modelformset_factory(
            Budget_Transaction, form=BudgetTransactionForm, extra=1
        )
        if request.method == "POST":
            formset = BudgetTransactionFormset(request.POST)
            if formset.is_valid():
                formset.save()
                return HttpResponseRedirect(reverse("budgeting_app:all_transactions"))
