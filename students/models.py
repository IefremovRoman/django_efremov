from django.db import models
from django.core.validators import RegexValidator

from groups.models import Group

phone_validation_message = "Phone number must be entered in the format: '+999999999'. \
                            Up to 15 digits allowed."


class Student(models.Model):
    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)
    age = models.IntegerField(default=0)
    phone = models.CharField(
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{12,15}$',
                message=phone_validation_message,
                code='invalid'
            )
        ],
        default='+00000000000000',
        max_length=15,
        blank=True
    )
    group_id = models.ForeignKey(
        Group,
        blank=True,
        default=None,
        on_delete=models.CASCADE)

    # def group_id(self):
    #     pass

    def __str__(self):
        return f'{self.id} \
                    {self.first_name} \
                    {self.last_name} \
                    {self.age} \
                    {self.phone} \
                    {self.group_id}'


# {self.Group.objects.filter(id=self.group_id)}

class Logger(models.Model):
    method = models.CharField(max_length=12)
    path = models.CharField(max_length=50)
    execution_time = models.FloatField(null=False)
    created = models.DateTimeField(auto_now_add=True)
