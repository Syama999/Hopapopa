from django.db import models

# Create your models here.
class Cloth(models.Model):
    title = models.CharField(max_length=200,verbose_name = 'Название')
    slug = models.SlugField(max_length=200, verbose_name='URL', unique=True)
    description = models.CharField(max_length=300,verbose_name = 'Описание', blank=True)
    colour = models.ForeignKey('Colour', on_delete=models.PROTECT, max_length=100,verbose_name = 'Цвет')
    price = models.IntegerField(verbose_name='Цена')
    size = models.ManyToManyField('Size', max_length=50, verbose_name = 'Размер')
    city_from = models.ForeignKey('City', on_delete=models.PROTECT, max_length=200, verbose_name = 'Cтрана производства')
    brand = models.ForeignKey('Brands', on_delete=models.PROTECT, max_length=200, verbose_name = 'Бренд')
    collection = models.ForeignKey('Collection', on_delete=models.PROTECT,max_length=200,verbose_name = 'Коллекция')
    type = models.ForeignKey('Type', on_delete=models.PROTECT, max_length=200,verbose_name = 'Тип')
    sex = models.ForeignKey('Sex', on_delete=models.PROTECT, max_length=200,verbose_name = 'Пол')
    style = models.ForeignKey('Style', on_delete=models.PROTECT, max_length=200,verbose_name = 'Стиль')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    class Meta:
        verbose_name = 'Cloth'
        verbose_name_plural = "Clothes"

    def __str__(self):
        return self.title
class Brands(models.Model):
    title = models.CharField(max_length = 200, verbose_name = "Название бренда")
    description = models.CharField(max_length = 200, verbose_name = "Описание", blank=True)
    class Meta:
        verbose_name = 'Brands'
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.title
class Collection(models.Model):
    title = models.CharField(max_length = 200, verbose_name = "Название коллекции")
    description = models.CharField(max_length=200, verbose_name="Описание", blank=True)


    def __str__(self):
        return self.title
class Style(models.Model):
    title = models.CharField(max_length = 200, verbose_name = "Название стиля")
    description = models.CharField(max_length=200, verbose_name="Описание", blank=True)


    def __str__(self):
        return self.title
class Type(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название коллекции")
    description = models.CharField(max_length=200, verbose_name="Описание", blank=True)

    def __str__(self):
        return self.title
    def __str__(self):
        return self.title
class Sex(models.Model):
    title = models.CharField(max_length=200, verbose_name='Пол')
    class Meta:
        verbose_name = 'Sex'
        verbose_name_plural = "Sex"

    def __str__(self):
        return self.title
class Colour(models.Model):
    title = models.CharField(max_length=200, verbose_name='Цвета')

    def __str__(self):
        return self.title
class City(models.Model):
    title = models.CharField(max_length=200, verbose_name='Произведено')
    description = models.CharField(max_length=200, verbose_name="Описание", blank=True)
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.title
class Size(models.Model):
    title = models.CharField(max_length=200, verbose_name='Размер')

    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = "Size"

    def __str__(self):
        return self.title