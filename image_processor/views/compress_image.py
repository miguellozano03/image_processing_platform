from django.http import FileResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.exceptions import NotFound, PermissionDenied

from image_processor.serializers import (
    ImageCompressSerializer,
    ImageExistingConvertSerializer,
)
from image_processor.processors.compressor import compress_img
from image_manager.models import Image as ImageModel


class AnonymousImageCompress(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = ImageCompressSerializer
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        image = serializer.validated_data["image"]

        try:
            buffer = compress_img(image)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return FileResponse(
            buffer,
            content_type=f"image/{image.image.format.lower()}",
            filename=image.name,
        )


class AuthCompressImage(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ImageExistingConvertSerializer
    parser_classes = [FormParser]

    def post(self, request, pk):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            image_obj = ImageModel.objects.get(pk=pk)
        except ImageModel.DoesNotExist:
            raise NotFound("Image not found")

        if image_obj.owner != request.user:
            raise PermissionDenied("It isn't your image")
 
        buffer = compress_img(image_obj.file)

        ext = image_obj.file.name.split(".")[-1].lower()

        return FileResponse(
            buffer,
            content_type=f"image/{ext}",
            filename=image_obj.file.name,
        )