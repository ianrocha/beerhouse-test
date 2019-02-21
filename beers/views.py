from rest_framework.viewsets import ModelViewSet

from .serializers import BeerSerializer
from .models import Beer


class BeerViewSet(ModelViewSet):
    serializer_class = BeerSerializer
    queryset = Beer.objects.all()
    lookup_field = 'name'

