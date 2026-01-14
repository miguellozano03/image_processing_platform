from rest_framework import serializers
from image_processor.processors.filters import FILTERS
from image_processor.processors.converter import CONVERT_OPTIONS

class BaseImageSerializer(serializers.Serializer):
    image = serializers.ImageField()

class ImageFilterSerializer(BaseImageSerializer):
    filter = serializers.ChoiceField(
        choices=list(FILTERS.keys()),
        help_text="Filter to apply to the image. Choose from available options."
    )

class ImageExistingFilterSerializer(serializers.Serializer):
     filter = serializers.ChoiceField(
        choices=list(FILTERS.keys()),
        help_text="Filter to apply to the image. Choose from available options."
    )

class ImageConvertSerializer(BaseImageSerializer):
    format = serializers.ChoiceField(
        choices=list(CONVERT_OPTIONS.keys()),
        help_text="Format output to convert. Choose from available options."
    )

class ImageExistingConvertSerializer(serializers.Serializer):
    format = serializers.ChoiceField(
        choices=list(CONVERT_OPTIONS.keys()),
        help_text="Format output to convert. Choose from available options."
    )

class ImageCompressSerializer(BaseImageSerializer):
    pass