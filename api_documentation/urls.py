from api_documentation.views import (
    ApiDocsSchemaView,
    ApiDocsSwaggerView,
    ApiDocsRedocView
)

from django.urls import path


urlpatterns = [
    path('schema/', ApiDocsSchemaView.as_view(), name='schema'),
    path('schema/docs/', ApiDocsSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', ApiDocsRedocView.as_view(url_name='schema'), name='redoc'),
]