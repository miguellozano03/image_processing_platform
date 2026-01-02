from django.urls import path

from image_manager.views import UploadAndListImagesView

urlpatterns = [
    path('images/upload', UploadAndListImagesView.as_view(), name='upload/list-image')
]