from django.urls import path
from image_processor.views.filter_apply import AnonymousImageFilterApply, ImageFilterApply
from image_processor.views.convert_format import AnonymousImageConvert, AuthImageConvert
from image_processor.views.compress_image import( 
    AnonymousImageCompress,
    AuthCompressImage
)

urlpatterns = [
    path("images/filters/", AnonymousImageFilterApply.as_view(), name="image-filter-anon"),
    path("images/filters/<int:pk>", ImageFilterApply.as_view(), name='image-filter-auth'),

    path("images/convert/", AnonymousImageConvert.as_view(), name='image-convert'),
    path("images/convert/<int:pk>", AuthImageConvert.as_view(), name='image-convert-auth'),

    path("images/compress/", AnonymousImageCompress.as_view(), name='image-compress'),
    path("images/compress/<int:pk>", AuthCompressImage.as_view(), name='image-compress-auth'),
]