from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiParameter

from image_manager.models import Image
from image_manager.serializers import ImageSerializer


class UploadAndListImagesView(ListCreateAPIView):
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

    @extend_schema(
        description=(
            "List all images uploaded by the authenticated user.\n\n"
            "Only images owned by the current user are returned."
        ),
        responses={200: ImageSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        description=(
            "Upload a new image.\n\n"
            "The uploaded image will be associated with the authenticated user."
        ),
        request=ImageSerializer,
        responses={
            201: ImageSerializer,
            400: OpenApiResponse(description="Invalid image data"),
        },
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get_queryset(self):  # pyright: ignore[reportIncompatibleMethodOverride]
        return Image.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DeleteImageView(DestroyAPIView):
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

    @extend_schema(
        description="Delete one of your uploaded images.",
        parameters=[
            OpenApiParameter(
                name="pk",
                type=int,
                location=OpenApiParameter.PATH,
                description="ID of the image owned by the authenticated user",
                required=True,
            )
        ],
        responses={
            204: OpenApiResponse(description="Image deleted successfully"),
            404: OpenApiResponse(description="Image not found"),
        },
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_queryset(self):  # pyright: ignore[reportIncompatibleMethodOverride]
        return Image.objects.filter(owner=self.request.user)
