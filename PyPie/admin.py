from django.contrib.admin import AdminSite

from pie.models import Pie
from pie_run.models import PieRun
from pie_run_order.models import PieRunOrder, PieRunOrderEntry


class PiePyAdminSite(AdminSite):
    site_header = "Pie Runner Admin"


admin_site = PiePyAdminSite(name="Pie Runner Admin")
admin_site.register([Pie, PieRun, PieRunOrder, PieRunOrderEntry])
