from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Имя'
    )
    email = models.EmailField(
        verbose_name = "Почта"
    )
    subject = models.CharField(
        max_length = 255,
        verbose_name = 'Тема'
    )
    message = models.TextField(
        verbose_name = 'Сообщение'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'


class Bron(models.Model):
    fullname = models.CharField(
        max_length = 255,
        verbose_name = 'Полное имя'
    )
    email = models.EmailField(
        verbose_name = "Почта"
    )
    phone = models.CharField(
        max_length = 255,
        verbose_name = 'Номер телефона'
    )
    date = models.CharField(
        max_length = 255,
        verbose_name = 'Дата'
    )
    message = models.TextField(
        verbose_name = 'Сообщение'
    )

    def __str__(self):
        return self.fullname
    
    class Meta:
        verbose_name = 'Брон'
        verbose_name_plural = 'Брон'
