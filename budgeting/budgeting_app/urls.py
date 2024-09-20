from django.urls import path
from . import views

app_name = "budgeting_app"
urlpatterns = [
    path(
        "group_details/<int:pk>/",
        views.Group_Detail_View.as_view(),
        name="group_detail",
    ),
    path("all_groups/", views.All_Groups_View.as_view(), name="all_groups"),
    # A site qwith the group creation action
    path("group_create/", views.Group_Create_View.as_view(), name="group_create"),
    # Group creation post action
    path("create_group/", views.create_group, name="create_group"),
    path("edit_group/<int:pk>/", views.edit_group, name="edit_group"),
    path("delete_group/<int:pk>/", views.delete_group, name="delete_group"),
]
