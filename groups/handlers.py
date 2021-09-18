from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Group
from students.models import Student


# @receiver(pre_save, sender=Student)
# def phone_edit_handler(sender, **kwargs):
#     if phone := kwargs['instance'].phone:
#         kwargs['instance'].phone = int(phone.strip('').replace('+', '').replace('(', '').replace(')', ''))


@receiver(post_save, sender=Student)
def student_counter(sender, instance, **kwargs):
    try:
        obj = sender.objects.get(group_id=instance.group_id)
    except:
        print('Something goes wrong')
    else:
        if obj.group_id != instance.group_id:
            group = Group.objects.filter(id=obj.group_id).values()[0]
            group.student_quantity = len(sender.objects.get(group_id=obj.group_id))
            # get('student_quantity')
    # if first_name := kwargs['instance'].first_name:
    # 	kwargs['instance'].first_name = first_name.capitalize()
    # if last_name := kwargs['instance'].last_name:
    # 	kwargs['instance'].last_name = last_name.capitalize()
