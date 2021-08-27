from django.db import models
from django.core.validators import RegexValidator


phone_valitation_message = "Phone number must be entered in the format: '+999999999'. \
                            Up to 15 digits allowed."

class Student(models.Model):
    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)
    age = models.IntegerField(default=0)
    phone = models.CharField(
                                validators=[
                                                RegexValidator(
                                                                regex=r'^\+?1?\d{12,15}$',
                                                                message=phone_valitation_message,
                                                                code='invalid'
                                                                )
                                ],
                                default='+00000000000000',
                                max_length=15,
                                blank=True
                            )

    def __str__(self):
        return f'{self.id} \
                    {self.first_name} \
                    {self.last_name} \
                    {self.age} \
                    {self.phone}'


class Logger(models.Model):
    method = models.CharField(max_length=12)
    path = models.CharField(max_length=50)
    execution_time = models.TimeField(null=False)
    created = models.DateTimeField(auto_now_add=True)
