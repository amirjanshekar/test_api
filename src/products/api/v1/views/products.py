from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from products.models import Product
from products.api.v1.serializers import ProductsSerializer
from products.api.v1.filters import ProductsFilter


@permission_classes([AllowAny])
class ProductsListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    filterset_class = ProductsFilter

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)

        Product.objects.bulk_create([Product(**item) for item in serializer.validated_data])

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        return Product.objects.all()
