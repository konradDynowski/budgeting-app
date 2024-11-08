import calendar

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from datetime import date
from django.urls import resolve
from ..forms import BudgetTransactionForm, FilterAllTransactions
from django.forms import modelformset_factory
from ..models import Budget_Transaction, Budget_Category
from budgeting_app.helpers import csv_to_transaction_helpers
from django.shortcuts import render
from ..forms import Csv_Transaction_Form

class AllTransactionsView(generic.ListView):
    template_name = "budgeting_app/transaction_templates/all_transactions.html"
    form_class = BudgetTransactionForm
    context_object_name = "all_txns"

    def get_queryset(self):
        queryset = Budget_Transaction.objects.filter(active_flag__exact=True)
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

class TransactionDetails(generic.UpdateView, generic.DetailView):
    model = Budget_Transaction
    template_name = "budgeting_app/transaction_templates/update_transaction.html"
    fields = ["transaction_date", "transaction_amount", "transaction_description"]
    
    def form_valid(self, form):
        current_url = self.request.path
        form.save()
        return HttpResponseRedirect(current_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["transaction"] = context["object"]
        return context

def delete_transaction(request, **kwargs):
    if request.method == "POST":
        transaction = Budget_Transaction.objects.get(pk=kwargs["pk"])
        transaction.active_flag = False
        transaction.save()
        year = transaction.transaction_date.year
        month = transaction.transaction_date.month
        date_to = date(year, month, 1)
        date_from = date(year, month, calendar.monthrange(year, month)[1])
        return HttpResponseRedirect(reverse("budgeting_app:all_transactions"))

def upload_csv(request, **kwargs):
    template_name = "budgeting_app/transaction_templates/update_csv_transactions.html"
    csv_data = []
    if request.method == "POST":
        form = Csv_Transaction_Form(request.POST, request.FILES)

        if form.is_valid():
            csv_file = request.FILES["csv_file"].read().decode("utf-8")
            helper = csv_to_transaction_helpers.Csv_To_Transaction_Helper()
            csv_transactions = helper.proces_mbank_payload(csv_file)
            return render(request, "budgeting_app/transaction_templates/csv_transactions_preview.html",
                          {
                              "csv_transactions": csv_transactions,
                              "categories": Budget_Category.objects.all(),
                              } 
                          )

    else:
        form = Csv_Transaction_Form()
        return render(request, template_name, {"form": form})

def insert_transactions_from_csv_preview(request, **kwargs):
    if request.method == "POST":
        # POST has a dict with values, reflecting actual HTTP request
        
        transaction_information = {}
        for key, value in request.POST.items():
            # ignore csrf, not needed to initialize transaction
            if key == "csrfmiddlewaretoken":
                continue

            attribute_type = "".join([character for character in key if character.isalpha()])
            transaction_form_number = "".join([digit for digit in key if digit.isdigit()])

            # now insert/update transaction information
            if transaction_form_number in transaction_information.keys():
                transaction_information[transaction_form_number][attribute_type] = value
            else:
                transaction_information[transaction_form_number] = { attribute_type: value }

        # now create transactions into the database if there are any
        print(transaction_information)
        for key, transaction in transaction_information.items():
            txn = Budget_Transaction(
                    category_id=Budget_Category.objects.get(pk=transaction["transactionscategory"]),
                    transaction_date=transaction["transactionsdate"],
                    transaction_amount=float(transaction["transactionsamount"].replace(",", ".")),
                    transaction_description=transaction["transactionsdescription"],
                    transaction_external_comment=transaction["transactionsdescriptionlegacy"])
        txn.save()


        #transaction_definitions = request.POST["transactions"] 
        return render(request, "budgeting_app/transaction_templates/update_csv_transactions.html", {"form": Csv_Transaction_Form()})

    else:
        return render(request, "budgeting_app/transaction_templates/update_csv_transactions.html", {"form": Csv_Transaction_Form()})
