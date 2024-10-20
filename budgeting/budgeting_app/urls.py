from django.urls import path
from .views import group_views
from .views import category_views
from .views import budget_txn_views

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
]
