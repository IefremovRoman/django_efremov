import requests

from django.core.management.base import BaseCommand

from service_apps.models import Currency, CurrencyEUR, CurrencyUSD, CurrencyRUB

CURRENCY_CODES = {
    'USD': 840,
    'EUR': 978,
    'RUB': 643
}

UPDATED_CODES = CURRENCY_CODES.copy()
UPDATED_CODES.update({'RUR': 643})

CODES = {v: k for k, v in CURRENCY_CODES.items()}

ADDRESS = {
    'nbu': 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json',
    'mono': 'https://api.monobank.ua/bank/currency',
    'privat': 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'
}


class Command(BaseCommand):

    def handle(self, **options):
        nbu_data, mono_data, privat_data = {}, {}, {}
        bank_key = ['currency_nbu', 'currency_mono', 'currency_privat']
        db_data = dict.fromkeys(bank_key)
        usd_data, eur_data, rub_data = db_data.copy(), db_data.copy(), db_data.copy()

        nbu_json = requests.get(ADDRESS.get('nbu')).json()
        mono_json = requests.get(ADDRESS.get('mono')).json()
        privat_json = requests.get(ADDRESS.get('privat')).json()

        for cur in nbu_json:
            currency_label = cur.get('cc')
            if currency_label in CURRENCY_CODES.keys():
                nbu_data.update({currency_label: cur.get('rate')})

        for cur in mono_json:
            value_code = cur.get('currencyCodeA', None)
            if all([value_code in CODES.keys(),
                    cur.get('currencyCodeB', None) == 980]):
                mono_data.update({CODES.get(value_code): cur.get('rateBuy')})

        for cur in privat_json:
            currency_label = cur.get('ccy')
            if currency_label in UPDATED_CODES:
                if currency_label == 'RUR': currency_label = 'RUB'
                privat_data.update({currency_label: cur.get('buy')})

        usd_data = {b: v.get('USD') for b, v in zip(bank_key, [nbu_data, mono_data, privat_data])}
        eur_data = {b: v.get('EUR') for b, v in zip(bank_key, [nbu_data, mono_data, privat_data])}
        rub_data = {b: v.get('RUB') for b, v in zip(bank_key, [nbu_data, mono_data, privat_data])}

        current_usd_currency = CurrencyUSD.objects.create(**usd_data)
        current_eur_currency = CurrencyEUR.objects.create(**eur_data)
        current_rub_currency = CurrencyRUB.objects.create(**rub_data)
