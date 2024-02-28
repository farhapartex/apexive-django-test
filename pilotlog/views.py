from django.http import HttpResponse
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from pilotlog import serializers, models, utils


class PilotLogAPIViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.PilotLogSerializer

    def get_queryset(self):
        return models.PilotLog.objects.get_pilot_logs(self.request.user)

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        instance = self.get_object()
        try:
            response = HttpResponse(
                content_type='text/csv',
                headers={
                    'Content-Disposition': f'attachment; filename="{utils.generate_n_length_random_string(20)}.csv"'},
            )

            utils.prepare_csv_file(instance.file, response)

            return response
        except Exception as e:
            return HttpResponse("The file uploaded may have bugs, try with the sample attached file.", status=500)
