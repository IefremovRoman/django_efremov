from random import choice

from django.core.management.base import BaseCommand

from faker import Faker

from students.models import Student
from groups.models import Group


faker = Faker()


class Command(BaseCommand):
    def __init__(self):
        super(Command, self).__init__()
        self.help = 'Generate random students'

    def add_arguments(self, parser):
        parser.add_argument('total', nargs='?', type=int)

    def handle(self, *args, **kwargs):
        # count = kwargs.get('total', 100)
        count = kwargs.get('total') if kwargs.get('total') else 100
        groups = Group.objects.all()
        for i in range(count):
            student = Student(
                                first_name=faker.first_name(),
                                last_name=faker.last_name(),
                                age=faker.random_int(min=30, max=100),
                                phone=f'+38000{faker.msisdn()[0:7]}',
                                group_id=choice(groups)
                            )
            student.save()

        message = f'{count} student(s) successfully created!'
        self.stdout.write(self.style.SUCCESS(message))
