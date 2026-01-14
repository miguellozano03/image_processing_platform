from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.exceptions import NotFound, PermissionDenied

from image_processor.serializers import ImageConvertSerializer, ImageExistingConvertSerializer
from image_processor.processors.converter import convert_img
from image_manager.models import Image as ImageModel

class AnonymousImageConvert(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = ImageConvertSerializer
    parser_classes = [MultiPartParser, FormParser]


    def post(self, request, pk, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        image = serializer.validated_data["image"]
        format_key = serializer.validated_data["format"]

        try:
            buffer = convert_img(image, format_key)
        except ValueError:
            return Response(
                {"error": "Image or format invalid."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        return HttpResponse(
            buffer,
            content_type=f"image/{format_key}",
            headers={
                "Content-Disposition":
                f'attachment; filename="converted.{format_key}"'
            }
        )
    
class AuthImageConvert(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ImageExistingConvertSerializer
    parser_classes = [FormParser]

    def post(self, request, pk):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        format_key = serializer.validated_data["format"]

        try:
            image_obj = ImageModel.objects.get(pk=pk)
        except:
            raise NotFound("Image not found")
        
        if image_obj.owner != request.user:
            raise PermissionDenied("It isn't your image")
        
        try:
            buffer = convert_img(image_obj.file, format_key)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        return HttpResponse(
            buffer,
            content_type=f"image/{format_key}",
            headers={
                "Content-Disposition":
                f'attachment; filename="converted.{format_key}"'
            }
        )