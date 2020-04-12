from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse

from ..models import Recipe, Timing
from ..views import RecipeListView

class RecipeListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_recipes = 20
        timing = Timing.objects.create(title='forever')

        for recipe_id in range(number_of_recipes):
            Recipe.objects.create(
                name=f'Recipe_{recipe_id}',
                timing=timing
            )

    def test_view_url_at_desired_location(self):
        resp = self.client.get('/api/recipes/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_get_by_name(self):
        resp = self.client.get(reverse('recipelist'))
        self.assertEqual(resp.status_code, 200)

class RecipesDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_recipes = 20
        timing = Timing.objects.create(title='forever')

        for recipe_id in range(number_of_recipes):
            Recipe.objects.create(
                name=f'Recipe_{recipe_id}',
                timing=timing
            )

    def test_view_url_at_desired_location(self):
        resp = self.client.get('/api/recipes/1')
        self.assertEqual(resp.status_code, 200)
    
    def test_view_url_get_by_name(self):
        resp = self.client.get(reverse('recipedetail',kwargs={'pk':1}))
        self.assertEqual(resp.status_code, 200)