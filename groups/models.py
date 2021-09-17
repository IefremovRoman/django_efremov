from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from teachers.models import Teacher


# ["title", "start_year", "finish_year", "student_quantity"]
class Group(models.Model):
    title = models.CharField(max_length=8, default='')
    start_year = models.IntegerField(
        validators=[MinValueValidator(1984),
                    MaxValueValidator(2021)],
        null=True)

    finish_year = models.IntegerField(
        validators=[MinValueValidator(1984),
                    MaxValueValidator(2021)],
        null=True)

    student_quantity = models.IntegerField(
        validators=[MaxValueValidator(10)],
        default=1)

    teacher_id = models.ForeignKey(
                                    Teacher,
                                    blank=True,
                                    default=None,
                                    on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} \
                    {self.title} \
                    {self.teacher_id} \
                    {self.start_year} \
                    {self.finish_year} \
                    {self.student_quantity}'

    # def group_to_dict(self):
    #     return {
    #         'id'
    #     }

#{self.Teacher.objects.filter(id=self.teacher_id)}
