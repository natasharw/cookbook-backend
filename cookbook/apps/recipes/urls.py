from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from .views import RecipeListView, RecipeDetailView

router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    url(r'^', include(router.urls)),

    url(r'^recipes/', RecipeListView.as_view()),
    url(r'^recipes/<int:pk>', RecipeDetailView.as_view())
]
