from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Announcement(models.Model):
    """Модель объявления о пропаже/находке."""
    TYPE_CHOICES = (
        ('lost', 'Потерян'),
        ('found', 'Найден'),
    )
    STATUS_CHOICES = (
        ('open', 'Активно'),
        ('closed', 'Закрыто'),
    )

    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, verbose_name='Тип')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open', verbose_name='Статус')
    location = models.CharField(max_length=200, blank=True, verbose_name='Место')
    contact_info = models.CharField(max_length=200, verbose_name='Контактная информация')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='announcements', verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return f"{self.get_type_display()}: {self.title}"


class Photo(models.Model):
    """Фотография, привязанная к объявлению."""
    image = models.ImageField(upload_to='announcement_photos/', verbose_name='Изображение')
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='photos', verbose_name='Объявление')
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name='Загружено')

    def __str__(self):
        return f"Фото для {self.announcement.title}"