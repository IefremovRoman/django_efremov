from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Group
from students.models import Student


# @receiver(pre_save, sender=Student)
# def phone_edit_handler(sender, **kwargs):
#     if phone := kwargs['instance'].phone:
#         kwargs['instance'].phone = int(phone.strip('').replace('+', '').replace('(', '').replace(')', ''))

# @receiver(pre_save, sender=Student)
# def old_group(sender, **kwargs):
#     return kwargs['instance'].group_id



# @receiver(post_save, sender=Student)
# def student_counter(sender, **kwargs):
#     # asd = old_group()
#
#     if group_id := kwargs['instance'].group_id:
#         breakpoint()
#         try:
#             obj = sender.objects.filter(group_id=group_id)
#         except:
#             print('Something goes wrong')
#         else:
#             if obj.group_id != group_id:
#                 old_group = Group.objects.filter(id=obj.group_id).values()[0]
#                 new_group = Group.objects.filter(id=group_id).values()[0]
#                 old_group.student_quantity = len(sender.objects.get(group_id=obj.group_id))
#                 new_group.student_quantity = len(sender.objects.get(group_id=group_id))
            # get('student_quantity')


# @receiver(pre_save, sender=Student)
# def student_counter(sender, **kwargs):
#     if kwargs['instance'].group_id is None:
#         print(1)
#     else:
#         new_std = kwargs['instance']
#         print(2)
#         old_std = sender.objects.get(id=new_std.id)
#         # breakpoint()
#         if old_std.group_id != new_std.group_id:
#             old_students = [s for s in Student.objects.filter(group_id=old_std.group_id).values()]
#             new_students = [s for s in Student.objects.filter(group_id=new_std.group_id).values()]
#             old_std.group_id.student_quantity = len(old_students)
#             new_std.group_id.student_quantity = len(new_students)
#
