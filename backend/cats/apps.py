"""Конфигурация приложения cats."""
from django.apps import AppConfig


class CatsConfig(AppConfig):
    """Конфигурация приложения Cats."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cats'
