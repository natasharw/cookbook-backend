from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import RecipeListView, RecipeDetailView

router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    path('', include(router.urls)),
    path('recipes/', RecipeListView.as_view(), name='recipelist'),
    path('recipes/<int:pk>', RecipeDetailView.as_view(), name='recipedetail')
]
