from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic

from pie_run_order.models import PieRunOrder, PieRunOrderEntry


def add(request):
    pie_run_order = PieRunOrder(client_name=request.POST['client_name'],
                                pie_run_id=request.POST['pie_run_id'])
    pie_run_order.save()

    order_items = zip(request.POST.getlist("pie-id[]"),
                      request.POST.getlist("pie-count[]"))
    order_items = filter(lambda x: x[1] and int(x[1]) > 0, order_items)
    for pie_order in order_items:
        pie_run_order_entry = PieRunOrderEntry(pie_run_order=pie_run_order,
                                               pie_id=pie_order[0],
                                               quantity=pie_order[1])
        pie_run_order_entry.save()

    return redirect("pie_run_order:details", pie_run_order_id=pie_run_order.pie_run_order_id)


def details(request, pie_run_order_id):
    pie_run_order = get_object_or_404(PieRunOrder, pie_run_order_id=pie_run_order_id)
    pie_run_order_entries = PieRunOrderEntry.objects.filter(pie_run_order_id=pie_run_order_id)
    context = {
        "pie_run_order": pie_run_order,
        "pie_run_order_entries": pie_run_order_entries,
    }
    return render(request, "pie_run_order/details.html", context)


class DetailView(generic.DetailView):
    model = PieRunOrder
    context_object_name = "pie_run_order"
    template_name = "pie_run_order/details.html"
