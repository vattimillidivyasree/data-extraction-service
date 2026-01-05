from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import ExtractionJob, ExtractionResult
from .serializers import ExtractionJobSerializer


@api_view(["GET"])
def health_check(request):
    return Response({"status": "ok"})


@api_view(["POST"])
def create_extraction(request):
    job = ExtractionJob.objects.create(status="pending")

    # Dummy extracted data (as required by task)
    sample_data = [
        {
            "email": "john@example.com",
            "first_name": "John",
            "last_name": "Doe",
            "external_id": "EXT001",
        },
        {
            "email": "jane@example.com",
            "first_name": "Jane",
            "last_name": "Smith",
            "external_id": "EXT002",
        },
    ]

    for item in sample_data:
        ExtractionResult.objects.create(job=job, **item)

    job.status = "completed"
    job.record_count = len(sample_data)
    job.save()

    serializer = ExtractionJobSerializer(job)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def get_extraction(request, job_id):
    job = get_object_or_404(ExtractionJob, id=job_id)
    serializer = ExtractionJobSerializer(job)
    return Response(serializer.data)