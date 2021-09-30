from django.contrib import admin

# Register your models here.

from .models import CurrencyRUB, CurrencyUSD, CurrencyEUR


class CurrencyRegister(admin.ModelAdmin):
    list_display = ['currency_nbu', 'currency_mono', 'currency_privat', 'created_at']


@admin.register(CurrencyUSD)
class CurrencyUSDAdmin(CurrencyRegister):
    pass


@admin.register(CurrencyEUR)
class CurrencyEURAdmin(CurrencyRegister):
    pass


@admin.register(CurrencyRUB)
class CurrencyRUBAdmin(CurrencyRegister):
    pass
