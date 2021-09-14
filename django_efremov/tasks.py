from django.core.mail import send_mail

from celery import shared_task

from students.models import Logger

from datetime import datetime, timedelta


@shared_task
def clean_admin_logs():
    deletion_time = datetime.today() - timedelta(days=7)
    Logger.objects.filter(created__lte=deletion_time).delete()
    return 'Old logs deleted!'

@shared_task
def contact_us_send_mail(title, message, from_email, recipient_list):
    send_mail(
                title=title,
                message=message,
                from_email=from_email,
                recipient_list=recipient_list
                )
