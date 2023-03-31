from django.db import models

# Create your models here.
class Cloth(models.Model):
    title = models.CharField(max_length=200,verbose_name = 'Название')
    slug = models.SlugField(max_length=200, verbose_name='URL', unique=True)
    description = models.CharField(max_length=300,verbose_name = 'Описание')
    colour = models.CharField(max_length=100,verbose_name = 'Цвет')
    price = models.IntegerField(verbose_name='Цена')
    size = models.CharField(max_length=50, verbose_name = 'Размер')
    city_from = models.CharField(max_length=200, verbose_name = 'Город производства')
    brand = models.CharField(max_length=200, verbose_name = 'Бренд')
    collection = models.CharField(max_length=200,verbose_name = 'Коллекция')
    type = models.CharField(max_length=200,verbose_name = 'Тип')
    sex = models.CharField(max_length=200,verbose_name = 'Пол')
    style = models.CharField(max_length=200,verbose_name = 'Стиль')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
