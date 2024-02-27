from django.db import models
from core.base_models import BaseAppModel


class PilotLog(BaseAppModel):
    file = models.FileField(upload_to='pilot_logs/%Y/%m/%d/')

    class Meta:
        verbose_name = 'Pilot Log'
        verbose_name_plural = 'Pilot Logs'
