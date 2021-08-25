from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


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
    student_quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.id} {self.title} {self.start_year} {self.finish_year} {self.student_quantity}'

# Old style model as I thought that model Group going to work as many-to-many database relationship.
# class Group(models.Model):
#     student_id = models.IntegerField()
#     teacher_id = models.IntegerField()

#     def __str__(self):
#         return f'{self.id} {self.student_id} {self.teacher_id}'
