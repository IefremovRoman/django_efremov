from random import randint, choice
from string import ascii_uppercase
import json

from django.core.management import call_command
from django.urls import reverse
from django.forms.models import model_to_dict

import pytest

from faker import Faker

from .models import Student, Logger

from groups.models import Group

from teachers.models import Teacher

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


@pytest.fixture
@pytest.mark.django_db
def group_prep(request, teacher_prep):
    students_qnt = randint(1, 10)
    start_year = randint(1984, 2016)
    teacher = Teacher.objects.get(pk=1)
    group = Group(
        title=choice(ascii_uppercase) + '%02d' % (abs(start_year) % 100),
        start_year=start_year,
        finish_year=start_year + 5,
        student_quantity=students_qnt,
        teacher_id=teacher
    )
    group.save()


@pytest.fixture(params=['123456789123456789', '123456', '123456789n123'])
def invalid_phone_number(request):
    return request.param


@pytest.mark.django_db
def test_student_list(client):
    url = reverse('students:list')
    client.get(url)
    assert Student.objects.count() == 0


@pytest.mark.django_db
def test_get_student(client):
    id_ = 1
    url = reverse('students:get', kwargs={'student_id': id_})
    client.get(url)
    assert Student.objects.count() == 0


@pytest.mark.django_db
def test_generate_student(client, group_prep):
    url = reverse('students:generate')
    response = client.get(url)
    assert Student.objects.count() == 1


@pytest.mark.django_db
def test_generate_students(client, group_prep):
    n = 100
    url = reverse('students:multi-generate', kwargs={'qty': n})
    response = client.get(url)
    assert Student.objects.count() == n


@pytest.mark.django_db
def test_create_student_empty_base_case(client, group_prep):
    url = reverse('students:create')
    group = Group.objects.get(pk=1)
    data = {
            'id': 1,
            'first_name': 'Name',
            'last_name': 'Surname',
            'age': 18,
            'phone': '+12345678910111',
            'group_id': group.id
    }
    response = client.post(url, data)
    assert Student.objects.count() == 1


@pytest.mark.django_db
def test_create_student_full_base_case(client, group_prep):
    call_command('generate_students', total=1)
    data = model_to_dict(Student.objects.get(pk=1))
    url = reverse('students:create')
    response = client.post(url, data)
    assert response.status_code == 302


@pytest.mark.django_db
def test_student_creation_fails_on_invalid_phone(client, group_prep, invalid_phone_number):
    url = reverse('students:create')
    group = Group.objects.get(pk=1)
    data = {
            'id': 1,
            'first_name': 'Name',
            'last_name': 'Surname',
            'age': 18,
            'phone': invalid_phone_number,
            'group_id': group.id
    }
    response = client.post(url, data)
    assert Student.objects.count() == 0


@pytest.mark.django_db
def test_edit_student(client, group_prep):
    call_command('generate_students', total=1)
    url = reverse('students:edit', kwargs={'student_id': 1})
    group = Group.objects.get(pk=1)
    data = {
            'id': 1,
            'first_name': 'Name',
            'last_name': 'Surname',
            'age': 18,
            'phone': '+12345678910111',
            'group_id': group.id
    }
    client.post(url, data)
    assert Student.objects.count() == 1
    assert model_to_dict(Student.objects.get(pk=1)) == data


@pytest.mark.django_db
def test_student_edition_fails_on_invalid_phone(client, group_prep, invalid_phone_number):
    call_command('generate_students', total=1)
    url = reverse('students:edit', kwargs={'student_id': 1})
    group = Group.objects.get(pk=1)
    data = {
            'id': 1,
            'first_name': 'Name',
            'last_name': 'Surname',
            'age': 18,
            'phone': invalid_phone_number,
            'group_id': group.id
    }
    before_update = model_to_dict(Student.objects.get(pk=1))
    client.post(url, data)
    after_update = model_to_dict(Student.objects.get(pk=1))
    assert before_update == after_update
    assert after_update != data


@pytest.mark.django_db
def test_logging_admin_middleware(client):
    response = client.get('/admin/')
    assert response.status_code < 400
    assert Logger.objects.count() > 0







# @pytest.fixture()
# def fixture_1(request):
#     print("fixture1 setup")
#
#     def resource_teardown():
#         print("fixture1 teardwon")
#
#     request.addfinalizer(resource_teardown)
#
# @pytest.fixture()
# def fixture_2(request, fixture_1):
#     print("fixture2 setup")
#
#     def resource_teardown():
#         print("fixture2 teardwon")
#
#     request.addfinalizer(resource_teardown)
#
#
#
# def test_1_that_needs_resource(fixture_1):
#     print("test_1_that_needs_resource")
#
#
# def test_2_that_does_not(fixture_1, fixture_2):
#     print("test_2_that_does_not")
#
#
# def test_3_that_does_again(fixture_2):
#     print("test_3_that_does_again")




# @pytest.mark.django_db
# def test_view(client):
#    url = reverse('homepage-url')
#    response = client.get(url)
#    assert response.status_code == 200
