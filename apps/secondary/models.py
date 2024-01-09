from django.db import models
from django_resized import ResizedImageField
from ckeditor.fields import RichTextField 
# Create your models here.
class Slide(models.Model):
    backimage = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='imageback/',
        verbose_name="Фото бекграунд",
        blank = True, null = True
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='imagemain/',
        verbose_name="Фото анимация",
        blank = True, null = True
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Заголовок'
    )
    descriptions = models.TextField(
        verbose_name = 'Описание'
    )
    shef = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='shef_image/',
        verbose_name="Фото Шефа",
        blank = True, null = True
    )
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Имя Шефа'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'


class Achievement(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='main_photo/',
        verbose_name="Главное фото",
        blank = True, null = True
    )
    experience = models.CharField(
        max_length = 255,
        verbose_name = 'Опыт работы'
    )
    title = models.CharField(
        max_length =255,
        verbose_name = "Заголовок"
    )
    descriptions = models.TextField(
        verbose_name = 'Описание'
    )
    name1 = models.CharField(
        max_length =255,
        verbose_name = "Название"
    )
    mini_descriptions1 = models.TextField(
        verbose_name = 'Короткое описание'
    )
    name2 = models.CharField(
        max_length =255,
        verbose_name = "Название"
    )
    mini_descriptions2 = models.TextField(
        verbose_name = 'Короткое описание'
    )
    name3 = models.CharField(
        max_length =255,
        verbose_name = "Название"
    )
    mini_descriptions3 = models.TextField(
        verbose_name = 'Короткое описание'
    )
    name4 = models.CharField(
        max_length =255,
        verbose_name = "Название"
    )
    mini_descriptions4 = models.TextField(
        verbose_name = 'Короткое описание'
    )

    def __str__(self):
        return self.name1
    
    class Meta:
        verbose_name = "Достижение"
        verbose_name_plural = "Достижения"


class Bakery(models.Model):
    image =  ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='bakery_image/',
        verbose_name="Фото изделий",
        blank = True, null = True
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название изделия'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Кондитерские изделия"
        verbose_name_plural = "Кондитерские изделия"

class BigCategory(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название категории"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "1) Главная категория"
        verbose_name_plural = "1) Главная категория"


class Category(models.Model):
    big_category = models.ForeignKey(BigCategory,on_delete = models.CASCADE,verbose_name  = "Выбрать главную категорию")
    name = models.CharField(
        max_length=255, 
        verbose_name='Название категории'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '2) Дочерная категория'
        verbose_name_plural = '2) Дочерная категория'

class Menu(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='bakery_image/',
        verbose_name="Фото изделий",
        blank=True, null=True
    )
    title = models.CharField(
        max_length=255, 
        verbose_name='Название изделия'
    )
    price_now = models.CharField(
        max_length=255, 
        verbose_name='Цена сейчас'
    )
    price_before = models.CharField(
        max_length=255, 
        verbose_name='Цена раньше'
    )
    descriptions = models.TextField(
        verbose_name = 'Описание'
    )
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '3) Меню'
        verbose_name_plural = '3) Меню'

class Discount(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='bakery_image/',
        verbose_name="Фото изделий",
        blank=True, null=True
    )
    title = models.CharField(
        max_length=255, 
        verbose_name='Название изделия'
    )
    descriptions = models.TextField(
        verbose_name = 'Описание'
    )
    price_now = models.CharField(
        max_length=255, 
        verbose_name='Цена сейчас'
    )
    price_before = models.CharField(
        max_length=255, 
        verbose_name='Цена раньше'
    )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Скидки'
        verbose_name_plural = 'Скидки'


class Clients(models.Model):
    descriptions1 = models.TextField(
        verbose_name = 'Описание'
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='image/',
        verbose_name="Фотография",
        blank=True, null=True
    )

    def __str__(self):
        return self.descriptions1
    
    class Meta:
        verbose_name = 'Отзывы клиента'
        verbose_name_plural = 'Отзывы клиентов'

class ClientsInline(models.Model):
    place_info = models.ForeignKey(Clients, related_name='clients_words' , on_delete=models.CASCADE)
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Имя'
    )
    profation = models.CharField(
        max_length = 255,
        verbose_name = 'Профессия'
    )
    descriptions2 = models.TextField(
        verbose_name = 'Описание'
    )
    image2 = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='image/',
        verbose_name="Фотография",
        blank=True, null=True
    )
    class Meta:
        unique_together = ('place_info', 'name')


class AllFood(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='image_all/',
        verbose_name="Фотография",
        blank=True, null=True
    )

    class Meta:
        verbose_name = 'Десерт'
        verbose_name_plural = 'Десерты'

class LastPost(models.Model):
    descriptions = models.TextField(
        verbose_name = 'Описание'
    )
    instagram = models.ImageField(
        upload_to='instagram_image/',
        verbose_name = 'instagram URL'
    )
    location = models.CharField(
        max_length = 255,
        verbose_name = 'Локация'
    )
    email = models.EmailField(
        verbose_name = 'Почта'
    )
    contacts = RichTextField(
        verbose_name = 'Контакты'
    )

    def __str__(self):
        return self.location
    
    class Meta:
        verbose_name = 'Надавний пост'
        verbose_name_plural = 'Недавние посты'

class SlideAbout(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='imagelast/',
        verbose_name="Задняя фотография",
        blank=True, null=True
    )

    class Meta:
        verbose_name = 'Главное фото О нас'
        verbose_name_plural = 'Главное фото О нас'


class News(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='imagelast/',
        verbose_name="Фотография",
        blank=True, null=True
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = "Заголовок"
    )
    created_at = models.DateTimeField(
        auto_now_add = True,
        blank = True, null = True
    )
    descriprions = RichTextField(
        verbose_name = 'Описание'
    )
    letter = models.TextField(
        verbose_name = 'Комментарий'
    )
    mini_news = models.CharField(
        max_length =255,
        verbose_name = 'Доп новости'
    )
    mini_descriprions = RichTextField(
        verbose_name = 'Описание2'
    )
    image1 = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='image_news1/',
        verbose_name="Фотография",
        blank=True, null=True
    )
    image2 = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='image_news2/',
        verbose_name="Фотография",
        blank=True, null=True
    )
    comments = models.ManyToManyField('Review', related_name='news_comments', blank=True)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Последние Новости'
        verbose_name_plural = 'Последние Новости'

class Review(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Имя' 
    ) 
    email = models.EmailField(
        verbose_name = 'Почта'
    )
    comment = models.TextField(
        verbose_name = 'Комментарий'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class Food(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='bakery_image/',
        verbose_name="Фото изделий",
        blank=True, null=True
    )
    title = models.CharField(
        max_length=255, 
        verbose_name='Название изделия'
    )
    price_now = models.CharField(
        max_length=255, 
        verbose_name='Цена сейчас'
    )
    price_before = models.CharField(
        max_length=255, 
        verbose_name='Цена раньше'
    )
    descriptions = models.TextField(
        verbose_name = 'Описание'
    )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Еда в магазине'
        verbose_name_plural = 'Еда в магазине'
        

class Cart(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='image/',
        verbose_name="Фото изделий",
        blank=True, null=True
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название"
    )
    price = models.CharField(
        max_length=255, 
        verbose_name='Цена сейчас'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'


class Wishlist(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='image/',
        verbose_name="Фото изделий",
        blank=True, null=True
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название"
    )
    price = models.CharField(
        max_length=255,
        verbose_name='Цена сейчас'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Избранные'
        verbose_name_plural = 'Избранные'
