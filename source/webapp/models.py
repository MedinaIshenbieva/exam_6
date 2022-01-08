from django.db import models

# Create your models here.
STATUS_CHOICES = [('active', 'Активно'), ('blocked', 'Заблокировано')]


class GuestBook(models.Model):
    author = models.CharField(max_length=200, null=False, blank=False, verbose_name="Автор")
    email = models.EmailField(max_length=200, null=False, blank=False, verbose_name="Имейл")
    text = models.TextField(max_length=2000, null=False, blank=False, verbose_name="Текст записи")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата изменения")
    status = models.CharField(max_length=15, null=False, blank=False, default='active', choices=STATUS_CHOICES,
                              verbose_name="Статус")

    def __str__(self):
        return f"{self.pk}. {self.author} ({self.email})" \
               f"{self.text}"

    class Meta:
        db_table = 'guest_book'
        verbose_name = 'Гостевая книга'

