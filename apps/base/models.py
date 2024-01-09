from django.db import models
from django_resized import ResizedImageField
# Create your models here.
class Settings(models.Model):
    phone = models.CharField(
        max_length = 255,
        verbose_name = 'Телефонный номер'
    )
    logo = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='logo/',
        verbose_name="Логотип",
        blank = True, null = True
    )
    instagram = models.URLField(
        verbose_name = 'instagram URL'
    )
    dribbble = models.URLField(
        verbose_name = 'dribbble URL'
    )
    twitter = models.URLField(
        verbose_name = 'twitter URL '
    )
    youtube = models.URLField(
        verbose_name = ' youtube URL'
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='user_image/',
        verbose_name="Фото изделий",
        blank=True, null=True
    )
    def __str__(self):
        return self.phone
    
    class Meta:
         verbose_name = 'Настройка'
         verbose_name_plural = 'Настройки'



    