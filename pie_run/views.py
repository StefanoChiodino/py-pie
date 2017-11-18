from django.shortcuts import render, get_object_or_404

from pie.models import Pie
from pie_run.models import PieRun
from pie_run_order.models import PieRunOrder


def index(request):
    pie_runs = PieRun.objects.all()
    context = {
        'title': 'Pie Runs',
        'pie_runs': pie_runs
    }
    return render(request, 'pie_run/index.html', context)


def pie_run(request, pie_run_id):
    pie_run = get_object_or_404(PieRun, pie_run_id=pie_run_id)
    pie_run_orders = PieRunOrder.objects.filter(pie_run_id=pie_run_id)
    pies = Pie.objects.all()
    context = {
        'title': f'Pie Run {pie_run}',
        'pie_run': pie_run,
        'pie_run_orders': pie_run_orders,
        'pies': pies,
    }
    return render(request, 'pie_run/pie-run.html', context)
