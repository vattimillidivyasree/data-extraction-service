from rest_framework import serializers
from .models import ExtractionJob, ExtractionResult


class ExtractionResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtractionResult
        fields = "__all__"


class ExtractionJobSerializer(serializers.ModelSerializer):
    results = ExtractionResultSerializer(
        source="extractionresult_set", many=True, read_only=True
    )

    class Meta:
        model = ExtractionJob
        fields = [
            "id",
            "status",
            "record_count",
            "created_at",
            "finished_at",
            "results",
        ]
        read_only_fields = ["id", "status", "record_count", "created_at", "finished_at"]