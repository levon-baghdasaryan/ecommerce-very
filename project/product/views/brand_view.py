from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from ..models import Brand
from ..serializers import BrandSerializer


class BrandViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing all brands
    """

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        queryset = Brand.objects.all()
        serializer = BrandSerializer(queryset, many=True)
        return Response(serializer.data)
