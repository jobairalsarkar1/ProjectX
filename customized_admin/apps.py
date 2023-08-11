from django.apps import AppConfig


class CustomizedAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customized_admin'
