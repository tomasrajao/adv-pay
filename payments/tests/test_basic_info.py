import pytest
from django.urls import reverse
from model_bakery import baker

from payments.models import Company


@pytest.fixture
def company(db):
    return baker.make(Company)

@pytest.fixture
def resp(client, company):
    resp = client.get(reverse('payments:info', kwargs={'slug': company.slug}))
    return resp

def test_payments_page(resp, company):
    return resp.status_code == 200
