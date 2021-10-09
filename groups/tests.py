from random import choice, randint
from string import ascii_uppercase

from django.forms.models import model_to_dict
from django.urls import reverse

from faker import Faker

import pytest

from teachers.models import Teacher

from .models import Group

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
    return teacher


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
    return group


@pytest.mark.django_db
def test_group_list_empty_base(client):
    url = reverse('groups:list')
    response = client.get(url)
    assert response.status_code == 200
    assert Teacher.objects.count() == 0


@pytest.mark.django_db
def test_group_list_full_base(client, group_prep):
    url = reverse('groups:list')
    response = client.get(url)
    assert response.status_code == 200
    assert Teacher.objects.count() == 1


@pytest.mark.django_db
def test_get_group_empty_base(client):
    id_ = 1
    url = reverse('groups:get', kwargs={'group_id': id_})
    response = client.get(url)
    assert response.status_code == 200
    assert Teacher.objects.count() == 0


@pytest.mark.django_db
def test_get_group_full_base(client, group_prep):
    id_ = 1
    url = reverse('groups:get', kwargs={'group_id': id_})
    response = client.get(url)
    assert response.status_code == 200
    assert Teacher.objects.count() == 1


@pytest.mark.django_db
def test_create_group_empty_base_case(client, teacher_prep):
    url = reverse('groups:create')

    data = {
        'id': 1,
        'title': 'A00',
        'start_year': 2000,
        'finish_year': 2005,
        'student_quantity': 1,
        'teacher_id': teacher_prep.id
    }
    client.post(url, data)
    assert Group.objects.count() == 1


@pytest.mark.django_db
def test_create_group_full_base_case(client, group_prep):
    data = model_to_dict(group_prep)
    url = reverse('groups:create')
    response = client.post(url, data)
    assert response.status_code == 302


@pytest.mark.django_db
def test_edit_group(client, teacher_prep, group_prep):
    url = reverse('groups:edit', kwargs={'group_id': 1})
    data = {
        'id': 1,
        'title': 'A00',
        'start_year': 2000,
        'finish_year': 2005,
        'student_quantity': 1,
        'teacher_id': teacher_prep.id
    }
    client.post(url, data)
    assert Group.objects.count() == 1
    assert model_to_dict(Group.objects.get(pk=1)) == data


@pytest.mark.django_db
def test_group_deletion(client, group_prep):
    url = reverse('groups:delete', kwargs={'pk': 1})
    response = client.get(url)
    assert response.status_code == 302
    assert Group.objects.count() == 0
