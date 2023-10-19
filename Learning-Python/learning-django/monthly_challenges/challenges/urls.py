from django.urls import path
from . import views

urlpatterns = [
    # path("january", views.january), regular one by one path setting but down is dynamic and get anything
    path("", views.index, name="index"), # path for /challenges/ will be triggered
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
]

