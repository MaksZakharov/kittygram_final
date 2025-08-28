"""Вьюсеты для приложения cats."""

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Achievement, Cat
from .serializers import AchievementSerializer, CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Cat с поддержкой CRUD-операций."""

    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        """Сохраняет кота с текущим пользователем как владельцем."""
        serializer.save(owner=self.request.user)


class AchievementViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Achievement с поддержкой CRUD-операций."""

    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    pagination_class = None
