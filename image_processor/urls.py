from django.urls import path
from image_processor.views import AnonymousImageFilterApply, ImageFilterApply

urlpatterns = [
    path("processor", AnonymousImageFilterApply.as_view(), name="filter_processor"),
    path("processor/<int:pk>", ImageFilterApply.as_view(), name='auth_filter_processor')
]