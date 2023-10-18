from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .serializers import ProductSerializer, ProductOrderSerializer, OrderSerializer

@swagger_auto_schema(method="POST", request_body=ProductOrderSerializer)
@api_view(['POST'])
def register_order_product(request):
    """ Esse endpoint registra ordens de produção"""
    if request.method == 'POST':
        order_product_data = request.data
        print(order_product_data)
        serializer = ProductOrderSerializer(data=order_product_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

#------------------------------product------------------------------>
@swagger_auto_schema(method="POST", request_body=ProductSerializer)
@api_view(['POST'])
def create_product(request):
    """ Esse endpoint registra novos produtos """
    if request.method == 'POST':
        product_data = request.data
        serializer = ProductSerializer(data=product_data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201) 
        return Response(serializer.errors, status=400)  

    