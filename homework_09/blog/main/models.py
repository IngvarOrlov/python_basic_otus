from django.db import models


class User(models.Model):
    name = models.CharField(max_length=32, verbose_name="Имя пользователя")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время обновления")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        get_latest_by = ['created_at']


class Post(models.Model):
    title = models.CharField(max_length=64, verbose_name="Заголовок")
    body = models.TextField(verbose_name="Тело поста")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время обновления")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

