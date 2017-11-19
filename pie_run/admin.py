from django.contrib import admin

from pie_run.models import PieRun


class PieRunAdmin(admin.ModelAdmin):
    model = PieRun
    list_filter = ["date"]


admin.site.register(PieRun, PieRunAdmin)
