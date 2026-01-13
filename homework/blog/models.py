from django.db import models

class Feedback(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='Полное имя')
    email = models.EmailField(verbose_name='Электронная почта')
    text = models.TextField(verbose_name='Текст отзыва')
    checked = models.BooleanField(default=False)

    def __str__(self):
        return f"Отзыв от {self.full_name}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
