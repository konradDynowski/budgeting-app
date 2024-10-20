from django.urls import path
from .views import group_views
from .views import category_views
from .views import budget_txn_views

app_name = "budgeting_app"
urlpatterns = [
    path("", group_views.All_Groups_View.as_view(), name="index"),
    # Groups
    path(
        "group_details/<int:pk>/",
        group_views.Group_Detail_View.as_view(),
        name="group_detail",
    ),
    path("all_groups/", group_views.All_Groups_View.as_view(), name="all_groups"),
    path("", group_views.All_Groups_View.as_view(), name="all_groups"),
    # A site qwith the group creation action
    path("group_create/", group_views.Group_Create_View.as_view(), name="group_create"),
    # Group creation post action
    path("create_group/", group_views.create_group, name="create_group"),
    path("edit_group/<int:pk>/", group_views.edit_group, name="edit_group"),
    path("delete_group/<int:pk>/", group_views.delete_group, name="delete_group"),
    # Categories
    path(
        "category_details/<int:pk>/",
        category_views.Category_Detail_View.as_view(),
        name="category_detail",
    ),
    path(
        "all_categories/",
        category_views.All_Categories_View.as_view(),
        name="all_categories",
    ),
    # A site qwith the category creation action
    path(
        "category_create/",
        category_views.Category_Create_View.as_view(),
        name="category_create",
    ),
    # Category creation post action
    path("create_category/", category_views.create_category, name="create_category"),
    path("edit_category/<int:pk>/", category_views.edit_category, name="edit_category"),
    path(
        "delete_category/<int:pk>/",
        category_views.delete_category,
        name="delete_category",
    ),
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
]
