from django.urls import reverse
from django.utils import timezone

from django.test import TestCase, Client

from pie.models import Pie
from pie_run.models import PieRun
from pie_run_order.models import PieRunOrder, PieRunOrderEntry

CLIENT_NAME = "test client"
TEST_PIE_NAME = "test pie"

def add_test_pie_run_order():
    pie = Pie(name=TEST_PIE_NAME, price=1)
    pie.save()

    pie_run = PieRun(date=timezone.now())
    pie_run.save()

    pie_run_order = PieRunOrder(pie_run=pie_run,client_name=CLIENT_NAME)
    pie_run_order.save()

    pie_run_order_entry = PieRunOrderEntry(pie_run_order=pie_run_order, pie=pie, quantity=1)
    pie_run_order_entry.save()

    return pie_run_order_entry


class Test(TestCase):
    def test_details(self):
        pie_run_order_entry = add_test_pie_run_order()
        response = self.client.get(reverse("pie_run_order:details", args=(pie_run_order_entry.pie_run_order_id,)))
        self.assertIs(response.status_code, 200)

    def test_details_contains_client_name(self):
        pie_run_order_entry = add_test_pie_run_order()
        response = self.client.get(reverse("pie_run_order:details", args=(pie_run_order_entry.pie_run_order_id,)))
        self.assertContains(response, text=TEST_PIE_NAME, count=1)

    def test_details_contains_entries(self):
        pie_run_order_entry = add_test_pie_run_order()
        response = self.client.get(reverse("pie_run_order:details", args=(pie_run_order_entry.pie_run_order_id,)))
        self.assertContains(response, text=CLIENT_NAME, count=1)
