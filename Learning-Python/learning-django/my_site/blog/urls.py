from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="home-page"),
    path("posts", views.AllPostsView.as_view(), name="all-posts"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post-details"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later")
]
