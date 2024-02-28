from django.db import models


class PilotLogManager(models.Manager):
    def get_pilot_logs(self, pilot):
        return self.filter(pilot=pilot).order_by("-created_at")

    def get_latest_logs(self):
        return self.order_by("-created_at")
