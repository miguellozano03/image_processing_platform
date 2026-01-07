from rest_framework import serializers
from image_processor.processors.filter.filters import FILTERS

class AnonymousImageSerializer(serializers.Serializer):
    file = serializers.ImageField()
    filter = serializers.ChoiceField(
        choices=list(FILTERS.keys())
    )

class ApplyFilterSerializer(serializers.Serializer):
    filter = serializers.ChoiceField(
        choices=list(FILTERS.keys())
    )