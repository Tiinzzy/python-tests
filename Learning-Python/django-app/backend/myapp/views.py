from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item

@api_view(['GET'])
def get_items(request):
    items = Item.objects.all()
    data = [{'id': item.id, 'name': item.name} for item in items]
    return Response(data)

@api_view(['POST'])
def create_item(request):
    name = request.data.get('name')
    item = Item.objects.create(name=name)
    return Response({'id': item.id, 'name': item.name})