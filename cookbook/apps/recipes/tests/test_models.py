from django.test import TestCase
from django.utils import timezone
# from django.core.urlresolvers import reverse

from ..models import Recipe, Timing

class TimingModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Timing.objects.create(title='all afternoon')
    
    def test_title_label(self):
        timing = Timing.objects.get(title='all afternoon') 
        # fix to use get(id=1)
        field_label = timing._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')
    
    def test_title_max_length(self):
        timing = Timing.objects.get(title='all afternoon')
        # fix to use get(id=1)
        max_length = timing._meta.get_field('title').max_length
        self.assertEqual(max_length, 255)

    def test_object_name_is_title(self):
        timing = Timing.objects.get(title='all afternoon')
        # fix to use get(id=1)
        expected_object_name = str(timing.title)
        self.assertEquals(expected_object_name, str(timing))

class RecipeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        timing = Timing.objects.create(title='forever')
        Recipe.objects.create(name='something tasty', timing=timing)

    def test_name_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)
    
    def test_detail_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('detail').verbose_name
        self.assertEquals(field_label, 'detail')

    def test_detail_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('detail').max_length
        self.assertEqual(max_length, 1000)

    def test_object_name_is_name(self):
        recipe = Recipe.objects.get(id=1)
        expected_object_name = str(recipe.name)
        self.assertEquals(expected_object_name, str(recipe))