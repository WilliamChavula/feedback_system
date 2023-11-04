from django.urls import path

from . import views

app_name = "feedback"

urlpatterns = [
    path("", views.FeedbackListView.as_view(), name="list"),
    path("add/", views.AddFeedbackView.as_view(), name="add"),
    path("success/", views.AddFeedbackSuccessView.as_view(), name="success"),
]
