from django.db import models


class PilotLogManager(models.Manager):
    def get_latest_logs(self):
        return self.order_by("-created_at")
