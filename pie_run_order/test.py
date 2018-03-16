import uuid

import pytest
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


@pytest.mark.django_db
def test_add(client):
    pie = add_pie()
    pie_run = add_pie_run()
    data = {
        "client_name": CLIENT_NAME,
        "pie_run_id": pie_run.pie_run_id,
        "pie-id[]": pie.pie_id,
        "pie-count[]": 1,
    }
    response = client.post(reverse("pie_run_order:add"), data=data)
    # Make sure it redirects, we don't want page reloads to post this again.
    assert response.status_code == 302


@pytest.mark.django_db
def test_add_multiple_pies(client):
    pie = add_pie(TEST_PIE_NAME)
    pie2 = add_pie(TEST_PIE_NAME2)
    pie_run = add_pie_run()
    data = {
        "client_name": CLIENT_NAME,
        "pie_run_id": pie_run.pie_run_id,
        "pie-id[]": [pie.pie_id, pie2.pie_id],
        "pie-count[]": [1, 2],
    }
    response = client.post(reverse("pie_run_order:add"), data=data)
    # Make sure it redirects, we don't want page reloads to post this again.
    assert response.status_code == 302
    assert PieRunOrder.objects.count() == 1
    assert PieRunOrderEntry.objects.count() == 2


@pytest.mark.django_db
def test_details(client):
    pie_run_order_entry = add_test_pie_run_order()
    response = client.get(reverse("pie_run_order:details", args=(pie_run_order_entry.pie_run_order_id,)))
    assert response.status_code == 200


@pytest.mark.django_db
def test_details_contains_client_name(client):
    pie_run_order_entry = add_test_pie_run_order()
    response = client.get(reverse("pie_run_order:details", args=(pie_run_order_entry.pie_run_order_id,)))
    assert TEST_PIE_NAME in response.rendered_content


@pytest.mark.django_db
def test_details_contains_entries(client):
    pie_run_order_entry = add_test_pie_run_order()
    response = client.get(reverse("pie_run_order:details", args=(pie_run_order_entry.pie_run_order_id,)))
    assert CLIENT_NAME in response.rendered_content


@pytest.mark.django_db
def test_details_returns_404_if_not_found(client):
    response = client.get(reverse("pie_run_order:details", args=(uuid.uuid4(),)))
    assert response.status_code == 404
