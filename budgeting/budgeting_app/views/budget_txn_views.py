from django.shortcuts import render, redirect
from ..forms import BudgetTransactionForm
from django.forms import modelformset_factory
from ..models import Budget_Transaction


def add_transactions(request):
    BudgetTransactionFormSet = modelformset_factory(
        Budget_Transaction, form=BudgetTransactionForm, extra=1
    )

    if request.method == "POST":
        formset = BudgetTransactionFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect("success peaches")

    else:
        formset = BudgetTransactionFormSet(queryset=Budget_Transaction.objects.none())
    return render(
        request, "transaction_templates/add_transactions.html", {"formset": formset}
    )
