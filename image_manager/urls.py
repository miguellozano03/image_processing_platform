from django.urls import path

from image_manager.views import UploadAndListImagesView, DeleteImageView

urlpatterns = [
    path('images/', UploadAndListImagesView.as_view(), name='upload/list-image'),
    path('images/<int:pk>', DeleteImageView.as_view(), name='delete-image')
]