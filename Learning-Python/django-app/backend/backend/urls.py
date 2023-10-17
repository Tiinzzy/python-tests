from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo import views

router = routers.DefaultRouter()
router.register(r'todos', views.TodoView, 'todo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/sample/', views.sample_api, name='sample_api'),
    path('api/post/', views.post_data, name='post_data'),
    path('csrf-token/', views.get_csrf_token, name='get_csrf_token'),
]
