from django import forms
from .models import Budget_Category, Budget_Group, Budget_Transaction


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
            "transaction_date": forms.DateInput(
                attrs={"type": "date"}
            ),  # HTML5 date input
        }


class FilterAllTransactions(forms.Form):
    date_from = forms.DateField(
        required=True, label="Od", widget=forms.DateInput(attrs={"type": "date"})
    )
    date_to = forms.DateField(
        required=True, label="Do", widget=forms.DateInput(attrs={"type": "date"})
    )


class BudgetGroupForm(forms.ModelForm):
    class Meta:
        model = Budget_Group
        fields = [
            "id",
            "group_code",
            "group_name",
            "group_description",
        ]


class BudgetCategoryForm(forms.ModelForm):
    class Meta:
        model = Budget_Category
        fields = [
            "group_id",
            "category_code",
            "category_name",
            "category_description",
            "active_flag",
        ]
