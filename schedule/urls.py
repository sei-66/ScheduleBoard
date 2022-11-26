from django.urls import path


from . import views


urlpatterns = [
    path("schedule/", views.ScheduleBoardView.as_view()),
]
