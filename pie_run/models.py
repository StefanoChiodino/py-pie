import uuid

from django.db import models


class PieRun(models.Model):
    pie_run_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
