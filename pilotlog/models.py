from django.db import models
from django.contrib.auth.models import User
from core.base_models import BaseAppModel
from pilotlog.managers import PilotLogManager


class PilotLog(BaseAppModel):
    # add user table as foreign key named pilot
    pilot = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pilot_logs')
    file = models.FileField(upload_to='pilot_logs/%Y/%m/%d/')

    objects = PilotLogManager()

    class Meta:
        verbose_name = 'Pilot Log'
        verbose_name_plural = 'Pilot Logs'
