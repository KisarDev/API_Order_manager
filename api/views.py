from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, ProductOrder, Order
from .serializers import ProductSerializer, ProductOrderSerializer, OrderSerializer

@api_view(['POST'])
def register_order_product(request, produto: ProductOrderSerializer):
    if request.method == 'POST':
        order_product_data = request.data
        print(order_product_data)
        serializer = ProductOrderSerializer(data=order_product_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
@api_view(['POST'])
def create_product(request):
    if request.method == 'POST':
        product_data = request.data
        serializer = ProductSerializer(data=product_data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201) 
        return Response(serializer.errors, status=400)  

    