from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from .serializers import BeerSerializer
from .models import Beer


class BeerViewSet(ModelViewSet):
    serializer_class = BeerSerializer
    queryset = Beer.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'color', 'alcohol_content', 'temperature', 'ingredients')

