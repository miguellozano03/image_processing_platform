from rest_framework import serializers
from image_manager.models import Image

class ImageSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Image
        fields = ('id', 'owner', 'file', 'created_at')
        read_only_fields = ['id', 'created_at']

        extra_kwargs = {
            "name": {"help_text": "Name of the image"},
            "file": {"help_text": "Image file to upload"}
        }