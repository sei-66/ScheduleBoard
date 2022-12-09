from django.urls import path


from . import views


urlpatterns = [
    path("schedule/", views.ListScheduleView.as_view()),
    path("schedule/<int:pk>/detail", views.DetailScheduleView.as_view()),
]
