from django.db import models


class Group(models.Model):
    student_id = models.IntegerField()
    teacher_id = models.IntegerField()

    def __str__(self):
        return f'{self.id} {self.student_id} {self.teacher_id}'
