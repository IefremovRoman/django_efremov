# Generated by Django 3.2.6 on 2021-09-16 10:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_alter_teacher_phone'),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='teacher_id',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher'),
        ),
        migrations.AlterField(
            model_name='group',
            name='student_quantity',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10)]),
        ),
    ]
