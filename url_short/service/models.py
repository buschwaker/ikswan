import pyshorteners

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class URL(models.Model):
    """Модель Ссылка"""
    full_url = models.URLField(
        verbose_name='Ссылка',
        help_text='Введите ссылку',
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='urls',
        verbose_name='Пользователь',
    )

    @property
    def short_url(self):
        return pyshorteners.Shortener().clckru.short(self.full_url)

    class Meta:
        verbose_name_plural = 'Ссылки'
        verbose_name = 'Ссылка'
