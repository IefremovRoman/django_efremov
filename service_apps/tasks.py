from celery import shared_task

from django.core.management import call_command


@shared_task
def currency_parser():
    call_command('get_currencies')
