from rest_framework import serializers
from pilotlog.models import PilotLog


class PilotLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PilotLog
        fields = ('id', 'file', 'updated_at')

    def validate_file(self, value):
        """
        Check that the uploaded file is a .json file.
        """
        if not value.name.endswith('.json'):
            raise serializers.ValidationError("Only JSON files are allowed.")

        return value