from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
import json


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def save(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def edit(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def sample_api(request):
    print(request.body.decode('utf-8'))
    data = {"message": "Hello from Django!"}
    return JsonResponse(data)


def post_data(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        print(data)
        response_data = {"message": "Data received successfully."}
        return JsonResponse(response_data)


def get_csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})
