from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from pilotlog import serializers, models, utils


class PilotLogAPIViewSet(viewsets.ModelViewSet):
    queryset = models.PilotLog.objects.all()
    serializer_class = serializers.PilotLogSerializer

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        instance = self.get_object()
        response = HttpResponse(
            content_type='text/csv',
            headers={
                'Content-Disposition': f'attachment; filename="{utils.generate_n_length_random_string(20)}.csv"'},
        )

        utils.prepare_csv_file(instance.file, response)

        return response
