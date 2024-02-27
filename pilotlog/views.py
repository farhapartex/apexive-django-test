from rest_framework import viewsets
from pilotlog import serializers, models


class PilotLogAPIViewSet(viewsets.ModelViewSet):
    queryset = models.PilotLog.objects.all()
    serializer_class = serializers.PilotLogSerializer
