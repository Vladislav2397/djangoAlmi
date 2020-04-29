from django.db import models


class Category(models.Model):
    title = models.CharField('Название', max_length=150)
    subcategory = models.ManyToManyField(
        'self', verbose_name='Подкатегории', blank=True
    )

    def get_subcategories(self):
        return self.subcategory.all()

    def is_main_category(self):
        if self.subcategory.get(id=1):
            return True
        return False

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
