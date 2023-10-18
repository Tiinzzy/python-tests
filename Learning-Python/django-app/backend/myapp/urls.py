from django.urls import path
from .views import get_items, create_item

urlpatterns = [
    path('get-items/', get_items, name='get_items'),
    path('create-item/', create_item, name='create_item'),
]
