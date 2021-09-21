import json

from django.shortcuts import render

from .models import CurrencyEUR, CurrencyUSD, CurrencyRUB


# Create your views here.

def list_currencies(request):

    currency_list = {
        'USD': [c.prepare_to_json() for c in CurrencyUSD.objects.all()],
        'EUR': [c.prepare_to_json() for c in CurrencyEUR.objects.all()],
        'RUB': [c.prepare_to_json() for c in CurrencyRUB.objects.all()]
    }

    currencies_json = json.dumps(currency_list)
    fields = CurrencyEUR._meta.fields
    return render(
        request,
        'currency_table.html',
        {
            'json_currencies': currencies_json,
            'fields': fields
        }
    )
