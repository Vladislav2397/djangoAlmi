from django.db import models


# TODO: Product model - add field 'isTop' (boolean)
# TODO: Product model - add field 'pub_date' (date)
# TODO: Product detail - add analog table
# TODO: Create home page with carousel
# TODO: Create forum page


class Category(models.Model):
    title = models.CharField('Название', max_length=150)
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, verbose_name='Родитель',
        blank=True, null=True
    )

    isMain = models.BooleanField('Главная категория', default=False)
    isPackage = models.BooleanField('Пакет категорий', default=False)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    title = models.CharField('Название', max_length=200, null=True)
    description = models.TextField(
        'Описание', default='Для данного товара пока нет описания.'
    )

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True,
        verbose_name='Категория'
    )

    body = models.CharField('Корпус', max_length=30, null=True)
    producer = models.CharField('Производитель', max_length=30, null=True)
    price = models.FloatField('Цена')

    image = models.ImageField(
        'Изображение', upload_to='products/', blank=True
    )

    analog = models.ManyToManyField(
        'self', verbose_name='Аналоги', blank=True
    )

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
