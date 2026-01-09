from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)

class ApiDocsSchemaView(SpectacularAPIView):
    pass

class ApiDocsSwaggerView(SpectacularSwaggerView):
    pass

class ApiDocsRedocView(SpectacularRedocView):
    pass