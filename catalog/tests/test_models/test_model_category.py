from django.test import TestCase
from catalog.models import Category, Product
from django.db.models import CharField


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(title='test name')

    # ~~~~~~~~~~~~~~~ TITLE ~~~~~~~~~~~~~~~

    def test_title_field(self):
        category = Category.objects.get(id=1)

        title = category._meta.get_field('title').verbose_name
        self.assertEqual(title, 'Название')

        title = category._meta.get_field('title').blank
        self.assertFalse(title)

        title = category._meta.get_field('title')
        self.assertTrue(isinstance(title, CharField))

        title = category._meta.get_field('title').max_length
        self.assertEqual(title, 150)
