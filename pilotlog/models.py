from django.db import models
from core.base_models import BaseAppModel
from pilotlog.managers import PilotLogManager


class PilotLog(BaseAppModel):
    file = models.FileField(upload_to='pilot_logs/%Y/%m/%d/')

    objects = PilotLogManager()

    class Meta:
        verbose_name = 'Pilot Log'
        verbose_name_plural = 'Pilot Logs'
