from django.core.management import call_command

from celery import shared_task


@shared_task
def currency_parser():
    call_command('get_currencies')
