from django.core.management.base import BaseCommand

from faker import Faker

from students.models import Student


faker = Faker()


class Command(BaseCommand):
    def __init__(self):
        super(Command, self).__init__()
        self.help = 'Generate students'

    def add_arguments(self, parser):
        parser.add_argument('total', nargs='?', type=int)

    def handle(self, *args, **kwargs):
        # count = kwargs.get('total', 100)
        count = kwargs.get('total') if kwargs.get('total') else 100

        for i in range(count):
            Student.objects.create(
                                    first_name=faker.first_name(),
                                    last_name=faker.last_name(),
                                    age=faker.random_int(min=30, max=100)
                                    )

        message = f'{count} student(s) successfully created!'
        self.stdout.write(self.style.SUCCESS(message))
