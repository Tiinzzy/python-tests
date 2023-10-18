from django.urls import path
from . import views

urlpatterns = [
    path('get-items/', views.get_items, name='get_items'),
    path('create-item/', views.create_item, name='create_item'),
]
