from rest_framework import serializers
from image_processor.processors.filter.filters import FILTERS

class AnonymousImageSerializer(serializers.Serializer):
    file = serializers.ImageField(help_text="Image file to upload.")
    filter = serializers.ChoiceField(
        choices=list(FILTERS.keys()),
        help_text="Filter to apply to the image. Choose from available options."
    )

class ApplyFilterSerializer(serializers.Serializer):
    filter = serializers.ChoiceField(
        choices=list(FILTERS.keys()),
        help_text="Filter to apply to the image. Choose from available options"
    )