import json
from random import choice, randint
from string import ascii_uppercase

from django.core.management.base import BaseCommand
from django.core.management import call_command

from faker import Faker

from teachers.models import Teacher
from groups.models import Group

locale = 'uk_UA'
faker = Faker(locale)
json_file = 'teachers/management/commands/university_subjects.json'


class Command(BaseCommand):
    def __init__(self):
        super(Command, self).__init__()
        self.help = 'Generate teachers'

    def add_arguments(self, parser):
        parser.add_argument('total', nargs='?', type=int, default=100)

    def handle(self, total, *args, **kwargs):
        # count = kwargs.get('total', 100)
        # count = kwargs.get('total') if kwargs.get('total') else 100

        with open(json_file, 'r') as file:
            subjects = json.load(file)

        for t in range(total):
            teacher = Teacher(
                                first_name=faker.first_name(),
                                last_name=faker.last_name(),
                                age=faker.random_int(min=30, max=100),
                                subject=choice(subjects),
                                phone=f'+38000{faker.msisdn()[0:7]}'
            )
            teacher.save()
            students_qnt = randint(1, 10)
            start_year = randint(1984, 2016)
            group = Group(
                            title=choice(ascii_uppercase) + '%02d' % (abs(start_year) % 100),
                            start_year=start_year,
                            finish_year=start_year + 5,
                            student_quantity=students_qnt,
                            teacher_id=teacher
            )
            group.save()
            call_command('generate_students', total=students_qnt, group_id=group.id)

        message = f'{total} teacher(s) successfully created!'
        self.stdout.write(self.style.SUCCESS(message))
