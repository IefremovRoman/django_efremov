# Generated by Django 3.2.6 on 2021-08-12 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='student_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='group',
            name='teacher_id',
            field=models.IntegerField(),
        ),
    ]