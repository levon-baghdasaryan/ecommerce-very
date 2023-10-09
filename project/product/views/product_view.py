from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from ..models import Product
from ..serializers import ProductSerializer


class ProductViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing all products
    """

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
