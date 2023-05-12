from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_recipes, name='search_recipes'),
    path('recipe/<int:recipe_id>/', views.recipe_details, name='recipe_details'),
    path('recipe/<int:recipe_id>/save/', views.save_recipe, name='save_recipe'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
