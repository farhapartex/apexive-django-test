from rest_framework import serializers
from pilotlog.models import PilotLog


class PilotLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PilotLog
        fields = ('id', 'file')