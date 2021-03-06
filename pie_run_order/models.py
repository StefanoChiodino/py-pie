import uuid

from django.db import models

from pie.models import Pie
from pie_run.models import PieRun


class PieRunOrder(models.Model):
    pie_run_order_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    pie_run = models.ForeignKey(PieRun, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)

    def __str__(self):
        return str(f"{self.pie_run} - {self.client_name}")


class PieRunOrderEntry(models.Model):
    pie_run_order_entry_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    pie_run_order = models.ForeignKey(PieRunOrder, on_delete=models.CASCADE)
    pie = models.ForeignKey(Pie, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return str(F"{self.quantity} x {self.pie}")
