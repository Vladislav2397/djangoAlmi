from django.test import TestCase
from catalog.models import Product, Category
from django.db.models import (
    CharField, TextField, ForeignKey,
    FloatField, ImageField, ManyToManyField
)


class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(title='test name')
        Product.objects.create(
            title='test name', description='', category=category,
            body='test body', producer='test producer', price=123
        )

    # ~~~~~~~~~~~~~~~ TITLE ~~~~~~~~~~~~~~~

    def test_title_field(self):
        product = Product.objects.get(id=1)

        title = product._meta.get_field('title').verbose_name
        self.assertEqual(title, 'Название')

        title = product._meta.get_field('title').blank
        self.assertFalse(title)

        title = product._meta.get_field('title')
        self.assertTrue(isinstance(title, CharField))

        title = product._meta.get_field('title').max_length
        self.assertEqual(title, 200)

        title = product._meta.get_field('title').model
        self.assertEqual(title, Product)

        print(dir(product._meta.get_field('title')))

    # ~~~~~~~~~~~~~~~ DESCRIPTION ~~~~~~~~~~~~~~~

    def test_description_field(self):
        product = Product.objects.get(id=1)

        description = product._meta.get_field('description').verbose_name
        self.assertEqual(description, 'Описание')

        description = product._meta.get_field('description').blank
        self.assertFalse(description)

        description = product._meta.get_field('description')
        self.assertTrue(isinstance(description, TextField))

    # ~~~~~~~~~~~~~~~ CATEGORY ~~~~~~~~~~~~~~~

    def test_category_field(self):
        product = Product.objects.get(id=1)

        category = product._meta.get_field('category').verbose_name
        self.assertEqual(category, 'Категория')

        category = product._meta.get_field('category').blank
        self.assertFalse(category)

        category = product._meta.get_field('category')
        self.assertTrue(isinstance(category, ForeignKey))

    # ~~~~~~~~~~~~~~~ BODY ~~~~~~~~~~~~~~~

    def test_body_field(self):
        product = Product.objects.get(id=1)

        body = product._meta.get_field('body').verbose_name
        self.assertEqual(body, 'Корпус')

        body = product._meta.get_field('body').blank
        self.assertFalse(body)

        body = product._meta.get_field('body')
        self.assertTrue(isinstance(body, CharField))

        body = product._meta.get_field('body').max_length
        self.assertEqual(body, 30)

    # ~~~~~~~~~~~~~~~ PRODUCER ~~~~~~~~~~~~~~~

    def test_producer_field(self):
        product = Product.objects.get(id=1)

        producer = product._meta.get_field('producer').verbose_name
        self.assertEqual(producer, 'Производитель')

        producer = product._meta.get_field('producer').blank
        self.assertFalse(producer)

        producer = product._meta.get_field('producer')
        self.assertTrue(isinstance(producer, CharField))

        producer = product._meta.get_field('producer').max_length
        self.assertEqual(producer, 30)

    # ~~~~~~~~~~~~~~~ PRICE ~~~~~~~~~~~~~~~

    def test_price_field(self):
        product = Product.objects.get(id=1)

        price = product._meta.get_field('price').verbose_name
        self.assertEqual(price, 'Цена')

        price = product._meta.get_field('price').blank
        self.assertFalse(price)

        price = product._meta.get_field('price')
        self.assertTrue(isinstance(price, FloatField))

    # ~~~~~~~~~~~~~~~ IMAGE ~~~~~~~~~~~~~~~

    def test_image_field(self):
        product = Product.objects.get(id=1)

        image = product._meta.get_field('image').verbose_name
        self.assertEqual(image, 'Изображение')

        image = product._meta.get_field('image').blank
        self.assertTrue(image)

        image = product._meta.get_field('image')
        self.assertTrue(isinstance(image, ImageField))

    # ~~~~~~~~~~~~~~~ ANALOG ~~~~~~~~~~~~~~~

    def test_analog_field(self):
        product = Product.objects.get(id=1)

        analog = product._meta.get_field('analog').verbose_name
        self.assertEqual(analog, 'Аналоги')

        analog = product._meta.get_field('analog').blank
        self.assertTrue(analog)

        analog = product._meta.get_field('analog')
        self.assertTrue(isinstance(analog, ManyToManyField))
