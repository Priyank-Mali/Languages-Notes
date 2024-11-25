from .models import Products,ProductCategory
from .serializers import ProductSerializer,ProductCategorySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET','POST'])
def productCategoryList(request):
    if request.method == "GET":
        queryset = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(queryset,many=True)
        return Response({
            "data" : serializer.data
        },status=status.HTTP_200_OK)
    
    if request.method == "POST":
        jsondata = request.data
        serializer = ProductCategorySerializer(data=jsondata)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "data" : serializer.data
            },status=status.HTTP_201_CREATED)
        else:
            return Response({
                "error" : serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',"POST"])
def productList(request):
    if request.method == "GET":
        queryset = Products.objects.all()
        serializer = ProductSerializer(queryset,many=True)
        return Response({
            "data" : serializer.data
        },status=status.HTTP_200_OK)
    
    if request.method == "POST":
        jsondata = request.data
        serializer = ProductSerializer(data=jsondata)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "data" : serializer.data
            },status=status.HTTP_201_CREATED)
        else:
            return Response({
                "error" : serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)