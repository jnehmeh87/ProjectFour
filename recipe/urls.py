from . import views
from .views import AddRecipe, EditRecipe
# from recipe.views import add_recipe, edit_recipe
from django.urls import path


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('add/', views.AddRecipe.as_view(), name='add'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
    path('edit/<slug:slug>', views.EditRecipe.as_view(), name='edit_recipe'),
]
