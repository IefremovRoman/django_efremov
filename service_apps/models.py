from django.db import models


class Currency(models.Model):
    currency_nbu = models.DecimalField(max_digits=8, decimal_places=4, db_column='Currency NBU')
    currency_mono = models.DecimalField(max_digits=8, decimal_places=4, db_column='Currency Monobank')
    currency_privat = models.DecimalField(max_digits=8, decimal_places=4, db_column='Currency PrivatBank')
    created_at = models.DateTimeField(auto_now=True, db_column='Created at')


class CurrencyUSD(Currency):
    pass


class CurrencyEUR(Currency):
    pass


class CurrencyRUB(Currency):
    pass
