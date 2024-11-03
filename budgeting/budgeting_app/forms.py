from django import forms
from .models import Budget_Category, Budget_Group, Budget_Transaction
from .helpers import form_helpers

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
    category = form_helpers.fetch_categories_as_choice_field()


class GenerateQuotasForMonthForm(forms.Form):
    month = forms.ChoiceField(
        label="Miesiąc",
        choices=(
            (1, "Styczeń"),
            (2, "Luty"),
            (3, "Marzec"),
            (4, "Kwiecień"),
            (5, "Maj"),
            (6, "Czerwiec"),
            (7, "Lipiec"),
            (8, "Sierpień"),
            (9, "Wrzesień"),
            (10, "Październik"),
            (11, "Listopad"),
            (12, "Grudzień"),
        ),
        required=True,
    )
    year = forms.IntegerField(
        label="Rok", max_value=2100, min_value=2000, required=True
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
        ]


class Csv_Transaction_Form(forms.Form):
    csv_file = forms.FileField()
