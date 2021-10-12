from django.core.management import call_command
from django.forms.models import model_to_dict
from django.urls import reverse

from faker import Faker

import pytest

from teachers.models import Teacher

# from students.models import Student, Logger

# from groups.models import Group

# Help functions
faker = Faker()


@pytest.fixture()
@pytest.mark.django_db
def teacher_prep(request):
    teacher = Teacher(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        age=faker.random_int(min=30, max=100),
        subject='subject',
        phone=f'+38000{faker.msisdn()[0:7]}'
    )
    teacher.save()


# @pytest.fixture
# @pytest.mark.django_db
# def group_prep(request, teacher_prep):
#     students_qnt = randint(1, 10)
#     start_year = randint(1984, 2016)
#     teacher = Teacher.objects.get(pk=1)
#     group = Group(
#         title=choice(ascii_uppercase) + '%02d' % (abs(start_year) % 100),
#         start_year=start_year,
#         finish_year=start_year + 5,
#         student_quantity=students_qnt,
#         teacher_id=teacher
#     )
#     group.save()


@pytest.fixture(params=['123456789123456789', '123456', '123456789n123'])
def invalid_phone_number(request):
    return request.param


@pytest.mark.django_db
def test_teacher_list_empty_base(client):
    url = reverse('teachers:list')
    response = client.get(url)
    assert response.status_code == 200
    assert Teacher.objects.count() == 0


@pytest.mark.django_db
@pytest.mark.parametrize('n', [1, 10, 100])
def test_teacher_list_full_base(client, n):
    call_command('generate_teachers', total=n)
    url = reverse('teachers:list')
    response = client.get(url)
    assert response.status_code == 200
    assert Teacher.objects.count() == n


@pytest.mark.django_db
def test_get_teacher_empty_base(client):
    id_ = 1
    url = reverse('teachers:get', kwargs={'teacher_id': id_})
    response = client.get(url)
    assert response.status_code == 200
    assert Teacher.objects.count() == 0


@pytest.mark.django_db
@pytest.mark.parametrize('n', [1, 10, 100])
def test_get_teacher_full_base(client, n):
    call_command('generate_teachers', total=n)
    url = reverse('teachers:get', kwargs={'teacher_id': n})
    response = client.get(url)
    assert response.status_code == 200
    assert Teacher.objects.count() == n


@pytest.mark.django_db
def test_generate_teacher(client):
    url = reverse('teachers:generate')
    client.get(url)
    assert Teacher.objects.count() == 1


@pytest.mark.django_db
def test_generate_teachers(client):
    n = 100
    url = reverse('teachers:multi-generate', kwargs={'qty': n})
    client.get(url)
    assert Teacher.objects.count() == n


@pytest.mark.django_db
def test_create_teacher_empty_base_case(client):
    url = reverse('teachers:create')
    data = {
        'id': 1,
        'first_name': 'Name',
        'last_name': 'Surname',
        'age': 18,
        'subject': 'subject',
        'phone': '+12345678910111',
    }
    client.post(url, data)
    assert Teacher.objects.count() == 1


@pytest.mark.django_db
def test_create_teacher_full_base_case(client):
    call_command('generate_teachers', total=1)
    data = model_to_dict(Teacher.objects.get(pk=1))
    url = reverse('teachers:create')
    response = client.post(url, data)
    assert response.status_code == 302


@pytest.mark.django_db
def test_teacher_creation_fails_on_invalid_phone(client, invalid_phone_number):
    url = reverse('teachers:create')
    data = {
        'id': 1,
        'first_name': 'Name',
        'last_name': 'Surname',
        'age': 18,
        'subject': 'subject',
        'phone': invalid_phone_number,
    }
    client.post(url, data)
    assert Teacher.objects.count() == 0


@pytest.mark.django_db
def test_edit_teacher(client):
    call_command('generate_teachers', total=1)
    url = reverse('teachers:edit', kwargs={'teacher_id': 1})
    subject = 'subject'
    data = {
        'id': 1,
        'first_name': 'Name',
        'last_name': 'Surname',
        'age': 18,
        'subject': subject.capitalize(),
        'phone': '+12345678910111',
    }
    client.post(url, data)
    assert Teacher.objects.count() == 1
    assert model_to_dict(Teacher.objects.get(pk=1)) == data


@pytest.mark.django_db
def test_teacher_edition_fails_on_invalid_phone(client, invalid_phone_number):
    call_command('generate_teachers', total=1)
    url = reverse('teachers:edit', kwargs={'teacher_id': 1})
    data = {
        'id': 1,
        'first_name': 'Name',
        'last_name': 'Surname',
        'age': 18,
        'subject': 'subject',
        'phone': invalid_phone_number
    }
    before_update = model_to_dict(Teacher.objects.get(pk=1))
    client.post(url, data)
    after_update = model_to_dict(Teacher.objects.get(pk=1))
    assert before_update == after_update
    assert after_update != data


@pytest.mark.django_db
def test_teacher_deletion(client):
    call_command('generate_teachers', total=1)
    url = reverse('teachers:delete', kwargs={'pk': 1})
    response = client.get(url)
    assert response.status_code == 302
    assert Teacher.objects.count() == 0
