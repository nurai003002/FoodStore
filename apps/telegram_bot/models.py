from django.db import models
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
class TelegramUser(models.Model):
    id_user = models.CharField(
        max_length=100,
        verbose_name="ID пользователя telegram"
    )
    username = models.CharField(
        max_length=255,
        verbose_name="Имя пользователя",
        blank=True, null=True
    )
    first_name = models.CharField(
        max_length=255,
        verbose_name="Имя",
        blank=True, null=True
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name="Фамилия",
        blank=True, null=True
    )
    chat_id = models.CharField(
        max_length=100,
        verbose_name="Чат ID"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата регистрации"
    )
    slug = models.SlugField( 
        max_length=255,
        unique=True,
        db_index=True,
        blank=True, null=True
        )

    def get_absolute_url(self):
        return reverse('index',  kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.username)
    
    class Meta:
        verbose_name = "Пользователь телеграм"
        verbose_name_plural = "Пользователи телеграма"