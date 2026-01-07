import io
from PIL import Image as PilImage

from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.exceptions import NotFound, PermissionDenied

from image_processor.processors.filter.filters import FILTERS
from image_processor.serializers import AnonymousImageSerializer, ApplyFilterSerializer
from image_manager.models import Image as ImageModel

class AnonymousImageFilterApply(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = AnonymousImageSerializer
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        uploaded_file = serializer.validated_data["file"] # type: ignore
        filter_name = serializer.validated_data["filter"] # type: ignore

        img = PilImage.open(uploaded_file).convert("RGB")
        img = FILTERS[filter_name](img)

        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        response = HttpResponse(buffer, content_type="image/png")
        response["Content-Disposition"] = "attachment; filename=imagen.png"
        return response
    
class ImageFilterApply(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ApplyFilterSerializer
    parser_classes = [FormParser]

    def post(self, request, pk):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        filter_name = serializer.validated_data["filter"]

        try:
            image_obj = ImageModel.objects.get(pk=pk)
        except ImageModel.DoesNotExist:
            raise NotFound("Image not found")
        
        if image_obj.owner != request.user:
            raise PermissionDenied("It isn't your image")
        
        img = PilImage.open(image_obj.file.path).convert("RGB")
        img = FILTERS[filter_name](img)

        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        response = HttpResponse(buffer, content_type="image/png")
        response["Content-Disposition"] = (
            f'attachment; filename="image_{pk}_{filter_name}.png"'
        )

        return response