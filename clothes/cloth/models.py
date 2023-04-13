from django.db import models

# Create your models here.
class Cloth(models.Model):
    title = models.CharField(max_length=200,verbose_name = 'Название')
    slug = models.SlugField(max_length=200, verbose_name='URL', unique=True)
    description = models.CharField(max_length=300,verbose_name = 'Описание')
    colour = models.ForeignKey('Colour', on_delete=models.PROTECT, max_length=100,verbose_name = 'Цвет')
    price = models.IntegerField(verbose_name='Цена')
    size = models.CharField(max_length=50, verbose_name = 'Размер')
    city_from = models.ForeignKey('City', on_delete=models.PROTECT, max_length=200, verbose_name = 'Город производства')
    brand = models.ForeignKey('Brands', on_delete =models.PROTECT, max_length=200, verbose_name = 'Бренд')
    collection = models.ForeignKey('Collection', on_delete =models.PROTECT,max_length=200,verbose_name = 'Коллекция')
    type = models.ForeignKey('Type', on_delete =models.PROTECT, max_length=200,verbose_name = 'Тип')
    sex = models.ForeignKey('Sex', on_delete =models.PROTECT, max_length=200,verbose_name = 'Пол')
    style = models.ForeignKey('Style', on_delete =models.PROTECT, max_length=200,verbose_name = 'Стиль')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)


class Brands(models.Model):
    title = models.CharField(max_length = 200, verbose_name = "Название бренда")
    description = models.CharField(max_length = 200, verbose_name = "Описание")

class Collection(models.Model):
    title = models.CharField(max_length = 200, verbose_name = "Название коллекции")
    description = models.CharField(max_length=200, verbose_name="Описание")

class Style(models.Model):
    title = models.CharField(max_length = 200, verbose_name = "Название стиля")
    description = models.CharField(max_length=200, verbose_name="Описание")

class Type(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название коллекции")
    description = models.CharField(max_length=200, verbose_name="Описание")

class Sex(models.Model):
    title = models.CharField(max_length=200, verbose_name='Пол')
    description = models.CharField(max_length=200, verbose_name="Описание")

class Colour(models.Model):
    title = models.CharField(max_length=200, verbose_name='Цвета')

class City(models.Model):
    title = models.CharField(max_length=200, verbose_name='Произведено')
    description = models.CharField(max_length=200, verbose_name="Описание")