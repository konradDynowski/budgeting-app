from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from ..forms import BudgetTransactionForm
from django.forms import modelformset_factory
from ..models import Budget_Transaction


def add_transactions(request):
    BudgetTransactionFormSet = modelformset_factory(
        Budget_Transaction, form=BudgetTransactionForm, extra=1
    )

    if request.method == "POST":
        formset = BudgetTransactionFormSet(request.POST)
        print(formset.errors)
        if formset.is_valid():
            print("formset is valid")
            formset.save()
            return HttpResponseRedirect(
                reverse("budgeting_app:all_transactions")
            )
    else:
        formset = BudgetTransactionFormSet(queryset=Budget_Transaction.objects.none())
    return render(
        request,
        "budgeting_app/transaction_templates/add_transactions.html",
        {"formset": formset},
    )


class AllTransactionsView(generic.ListView):
    template_name = "budgeting_app/transaction_templates/all_transactions.html"
    context_object_name = "all_txns"

    def get_queryset(self):
        return Budget_Transaction.objects.all()