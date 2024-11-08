from django.urls import path
from .views import group_views
from .views import category_views
from .views import budget_txn_views
from .views import budget_quota_views

app_name = "budgeting_app"
urlpatterns = [
        path("", budget_quota_views.Quotas_Home_Page.as_view(), name="index"),
        path("<str:date_month>", budget_quota_views.Month_Home_Page.as_view(), name="month_index"),
        # Group
        path("all_groups/", group_views.All_Groups_View.as_view(), name="all_groups"),
        # Transactions
        path(
            "all_transactions/",
            budget_txn_views.AllTransactionsView.as_view(),
            name="all_transactions",
            ),
        path(
            "all_transactions/<str:date_from>/<str:date_to>/",
            budget_txn_views.AllTransactionsView.as_view(),
            name="all_transactions",
            ),
        # Categories
        path(
            "all_categories/",
            category_views.All_Categories_View.as_view(),
            name="all_categories",
            ),
        path(
            "plan_month/",
            budget_quota_views.GenerateBudgetView.as_view(),
            name="generate_budget",
            ),
        # should be like: 12-2024
        path(
            "month_planner/<str:date_month>/",
            budget_quota_views.PlanMonthView.as_view(),
            name="month_planning",
            ),
        path("transaction_details/<int:pk>/", budget_txn_views.TransactionDetails.as_view(), name="txn_details"),
        path("delete_transaction/<int:pk>", budget_txn_views.delete_transaction, name="delete_transaction"),
        path("upload_csv/", budget_txn_views.upload_csv, name="upload_csv"),
        path("upload_transactions_from_csv/", budget_txn_views.insert_transactions_from_csv_preview, name="upload_transactions_from_csv"),
        ]
