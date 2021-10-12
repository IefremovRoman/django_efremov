from datetime import datetime

from django.urls import reverse

import pytest

from .models import CurrencyEUR, CurrencyRUB, CurrencyUSD


@pytest.fixture
@pytest.mark.django_db
def currency_prep(request):
    # call_command('get_currencies')
    data = {
        'currency_nbu': 1,
        'currency_mono': 2,
        'currency_privat': 3,
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M')
    }
    CurrencyUSD.objects.create(**data)
    CurrencyEUR.objects.create(**data)
    CurrencyRUB.objects.create(**data)


@pytest.mark.django_db
def test_currency_list_empty_base(client):
    url = reverse('list-currencies')
    response = client.get(url)
    assert response.status_code == 200
    assert CurrencyUSD.objects.count() == 0
    assert CurrencyEUR.objects.count() == 0
    assert CurrencyRUB.objects.count() == 0


@pytest.mark.django_db
def test_currency_list_full_base(client, currency_prep):
    url = reverse('list-currencies')
    response = client.get(url)
    assert response.status_code == 200
    assert CurrencyUSD.objects.count() == 1
    assert CurrencyEUR.objects.count() == 1
    assert CurrencyRUB.objects.count() == 1
