from django.apps import AppConfig


class TeachersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'teachers'

    def ready(self):
        from .handlers import name_edit_handler  # noqa: F401