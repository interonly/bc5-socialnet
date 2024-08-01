from django.db import models
from django.contrib.auth.models import User


class Publication(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=200)
    content = models.TextField(verbose_name="Содержание")
    author = models.ForeignKey(
        to=User,
        verbose_name="Автор",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)

    def __str__(self):
        return self.title

