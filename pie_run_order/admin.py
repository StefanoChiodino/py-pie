from django.contrib import admin

from pie_run_order.models import PieRunOrder, PieRunOrderEntry

admin.site.register(PieRunOrder)
admin.site.register(PieRunOrderEntry)
