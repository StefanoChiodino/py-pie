from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from pies.models import PieRun, PieRunOrder


def index(request):
    pie_runs = PieRun.objects.all()
    context = {
        'title': 'Pie Runs',
        'pie_runs': pie_runs
    }
    return render(request, 'pies/index.html', context)


def pie_run(request, id):
    pie_run = PieRun.objects.get(pie_run_id=id)
    pie_run_orders = PieRunOrder.objects.filter(pie_run_id=id)
    context = {
        'title': f'Pie Run {pie_run}',
        'pie_run': pie_run,
        'pie_run_orders': pie_run_orders,
    }
    return render(request, 'pies/pie-run.html', context)
