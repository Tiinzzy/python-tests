from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank-you", views.ThanYouView.as_view()),
    path("reviews", views.ReviewsListView.as_view()),
]
