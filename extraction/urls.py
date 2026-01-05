from django.urls import path
from .views import health_check, create_extraction, get_extraction

urlpatterns = [
    path("health/", health_check),
    path("extractions/", create_extraction),
    path("extractions/<uuid:job_id>/", get_extraction),
]