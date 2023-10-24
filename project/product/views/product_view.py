from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
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

    @action(
        methods=["get"],
        detail=False,
        url_path=r"category/(?P<category>\w+)/all",
        url_name="all"
    )
    def list_product_by_category(self, request, category=None):
        """
        An endpoint to return products by category
        """
        serializer = ProductSerializer(
            Product.objects.filter(category__name=category), many=True
        )
        return Response(serializer.data)
