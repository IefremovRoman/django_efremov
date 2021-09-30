# Generated by Django 3.2.6 on 2021-08-27 05:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_alter_teacher_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.CharField(blank=True, default='+00000000000000', max_length=15, validators=[django.core.validators.RegexValidator(code='invalid', message="Phone number must be entered in the format: '+999999999'.                             Up to 15 digits allowed.", regex='^\\+?1?\\d{12,15}$')]),
        ),
    ]
