from django.db import models

# TODO: Product detail - add analog table
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
    isTop = models.BooleanField('Это хит продаж', default=False)
    pub_date = models.DateField('Дата публикации', null=True, blank=True)

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


class News(models.Model):
    title = models.CharField('Заголовок', max_length=200, null=True)
    description = models.TextField('Описание')
    pub_date = models.DateField('Дата публикации', null=True)
    image = models.ImageField(
        'Изображение', upload_to='news/',
        null=True, blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
