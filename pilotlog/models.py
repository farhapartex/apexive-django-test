from django.db import models
from core.base_models import BaseAbstractModel


class PilotLog(BaseAbstractModel):
    file = models.FileField(upload_to='pilot_logs/%Y/%m/%d/')

    class Meta:
        verbose_name = 'Pilot Log'
        verbose_name_plural = 'Pilot Logs'
