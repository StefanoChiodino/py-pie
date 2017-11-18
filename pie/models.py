import uuid

from django.db import models


class Pie(models.Model):
    pie_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name
