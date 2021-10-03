from django.core.validators import RegexValidator
from django.db import models

phone_valitation_message = "Phone number must be entered in the format: '+999999999'. \
                            Up to 15 digits allowed."


class Teacher(models.Model):
    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)
    age = models.IntegerField(default=0)
    subject = models.CharField(max_length=24)
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
                    {self.subject}\
                    {self.phone}'

    # def __dict__(self):
    #     return dict(id=self.id,
    #                 first_name=self.first_name,
    #                 last_name=self.last_name,
    #                 age=self.age,
    #                 subject=self.subject,
    #                 phone=self.phone)
