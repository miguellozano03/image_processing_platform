from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from image_manager.models import Image
from image_manager.serializers import ImageSerializer

class UploadAndListImagesView(ListCreateAPIView):
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self): # pyright: ignore[reportIncompatibleMethodOverride]
        return Image.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DeleteImageView(DestroyAPIView):
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self): # pyright: ignore[reportIncompatibleMethodOverride]
        return Image.objects.filter(owner=self.request.user)