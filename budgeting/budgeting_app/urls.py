from django.urls import path
from .views import group_views
from .views import category_views
from .views import budget_txn_views
from .views import budget_quota_views

app_name = "budgeting_app"
urlpatterns = [
    # Groups
    path("", group_views.All_Groups_View.as_view(), name="index"),
    path("all_groups/", group_views.All_Groups_View.as_view(), name="all_groups"),
    path("", group_views.All_Groups_View.as_view(), name="all_groups"),
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
]
