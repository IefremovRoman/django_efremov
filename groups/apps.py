from django.apps import AppConfig


class GroupsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'groups'

    # def ready(self):
    #     from .handlers import student_counter  # noqa: F401
