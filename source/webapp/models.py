from django.db import models

STATUS_CHOICES = (
    ('active', 'Активно'),
    ('blocked', 'Заблокировано'),
)


class Entry(models.Model):
    author = models.CharField(max_length=40, null=False, blank=False, default='Unknown', verbose_name='Имя автора')
    email = models.EmailField(null=False, blank=False, verbose_name='почта')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    status = models.CharField(max_length=30, null=False, blank=True, default=STATUS_CHOICES[0][0],
                              choices=STATUS_CHOICES, verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return self.text
