from rest_framework import serializers

from .models import Beer


class BeerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Beer
        fields = ('id', 'name', 'description', 'harmonization',
                  'color', 'alcohol_content', 'temperature',
                  'ingredients', 'image')
