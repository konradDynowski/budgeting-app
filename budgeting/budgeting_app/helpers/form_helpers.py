from ..models import *
from django import forms

def fetch_categories_as_choice_field():
    
    categories = Budget_Category.objects.filter(active_flag__exact=True)
    choices_tuples = (
        (category.id, str(category)) for category in categories
    )
    choices = forms.ChoiceField(
        choices=choices_tuples,
        required=False,
        label="Categories",
        label_suffix="cat",
    )
    return choices