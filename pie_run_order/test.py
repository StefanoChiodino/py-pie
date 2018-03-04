import uuid

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from pie.models import Pie
from pie_run.models import PieRun
from pie_run_order.models import PieRunOrder, PieRunOrderEntry

CLIENT_NAME = "test client"
TEST_PIE_NAME = "test pie"
TEST_PIE_NAME2 = "test pie"


def add_test_pie_run_order():
    pie = add_pie(TEST_PIE_NAME)
    pie_run = add_pie_run()

    pie_run_order = PieRunOrder(pie_run=pie_run,client_name=CLIENT_NAME)
    pie_run_order.save()

    pie_run_order_entry = PieRunOrderEntry(pie_run_order=pie_run_order, pie=pie, quantity=1)
    pie_run_order_entry.save()

    return pie_run_order_entry


def add_pie_run():
    pie_run = PieRun(date=timezone.now())
    pie_run.save()
    return pie_run


def add_pie(pie_name=TEST_PIE_NAME):
    pie = Pie(name=pie_name, price=1)
    pie.save()
    return pie


class TestAdd(TestCase):
    def test_add(self):
        pie = add_pie()
        pie_run = add_pie_run()
        data = {
            "client_name": CLIENT_NAME,
            "pie_run_id": pie_run.pie_run_id,
            "pie-id[]": pie.pie_id,
            "pie-count[]": 1,
        }
        response = self.client.post(reverse("pie_run_order:add"), data=data)
        # Make sure it redirects, we don't want page reloads to post this again.
        self.assertEqual(response.status_code, 302)

    def test_add_multiple_pies(self):
        pie = add_pie(TEST_PIE_NAME)
        pie2 = add_pie(TEST_PIE_NAME2)
        pie_run = add_pie_run()
        data = {
            "client_name": CLIENT_NAME,
            "pie_run_id": pie_run.pie_run_id,
            "pie-id[]": [pie.pie_id, pie2.pie_id],
            "pie-count[]": [1, 2],
        }
        response = self.client.post(reverse("pie_run_order:add"), data=data)
        # Make sure it redirects, we don't want page reloads to post this again.
        self.assertEqual(response.status_code, 302)
        self.assertEqual(PieRunOrder.objects.count(), 1)
        self.assertEqual(PieRunOrderEntry.objects.count(), 2)


class TestDetails(TestCase):
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

    def test_details_returns_404_if_not_found(self):
        response = self.client.get(reverse("pie_run_order:details", args=(uuid.uuid4(),)))
        self.assertEqual(response.status_code, 404)
