from django.utils import timezone
from django.core.mail import send_mail

from celery import shared_task

from .models import LogRecord

from datetime import timedelta


@shared_task
def clean_admin_logs():
	