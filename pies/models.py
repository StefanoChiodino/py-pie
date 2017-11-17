import uuid

from django.db import models


class Pie(models.Model):
    pie_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=10)

    def __str__(self):
        return self.name


class PieRun(models.Model):
    pie_run_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class PieRunOrder(models.Model):
    pie_run_order_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    pie_run = models.ForeignKey(PieRun)
    client_name = models.CharField(max_length=100)

    def __str__(self):
        return str(f"{self.pie_run} - {self.client_name}")


class PieRunOrderEntries(models.Model):
    pie_run_order = models.ForeignKey(PieRunOrder)
    pie = models.OneToOneField(Pie, primary_key=True)
    quantity = models.IntegerField()

    def __str__(self):
        return str(F"{self.quantity} x {self.pie}")
