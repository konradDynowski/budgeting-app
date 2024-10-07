from django import forms
from .models import Budget_Transaction


class BudgetTransactionForm(forms.ModelForm):
    class Meta:
        model = Budget_Transaction
        fields = [
            "category_id",
            "transaction_date",
            "transaction_amount",
            "transaction_description",
        ]
