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

    def create(self, validated_data):
        """
        Create and return a new `PilotLog` instance, given the validated data.
        """
        validated_data['pilot'] = self.context['request'].user
        return super().create(validated_data)