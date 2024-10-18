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
        widgets = {
            'transaction_date': forms.DateInput(attrs={'type': 'date'}),  # HTML5 date input
        }