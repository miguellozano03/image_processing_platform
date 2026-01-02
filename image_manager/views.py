from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from image_manager.models import Image
from image_manager.serializers import ImageSerializer
# Create your views here.

# class ListImagesView(ListAPIView):
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer
#     permission_classes = [IsAuthenticated]

# class UploadImageView(CreateAPIView):
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer
#     permission_classes = [IsAuthenticated]

class UploadAndListImagesView(ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]