from django.urls import path


from . import views


urlpatterns = [
    path("schedule/", views.ListScheduleView.as_view(), name="list-schedule"),
    path(
        "schedule/<int:pk>/detail",
        views.DetailScheduleView.as_view(),
        name="detail-schedule",
    ),
    path("schedule/create", views.CreateScheduleView.as_view(), name="create-schedule"),
    path(
        "schedule/<int:pk>/delete",
        views.DeleteScheduleView.as_view(),
        name="delete-schedule",
    ),
    path(
        "schedule/<int:pk>/update",
        views.UpdateScheduleView.as_view(),
        name="update-schedule",
    ),
]
