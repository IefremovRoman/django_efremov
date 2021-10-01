from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Teacher


@receiver(pre_save, sender=Teacher)
def name_edit_handler(sender, **kwargs):
    if first_name := kwargs['instance'].first_name:
        kwargs['instance'].first_name = first_name.capitalize()
    if last_name := kwargs['instance'].last_name:
        kwargs['instance'].last_name = last_name.capitalize()
    if subject := kwargs['instance'].subject:
        kwargs['instance'].subject = ' '.join(
            [s.capitalize() if s not in ['and', 'of'] else s for s in subject.split(' ')])
