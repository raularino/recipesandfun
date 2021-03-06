"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from RecipesAndFun.views import RecipeDetail
from RecipesAndFun import views
from RecipesAndFun.views import bienvenida

urlpatterns = [
    path('admin/', admin.site.urls),

    url('^$', views.bienvenida),

    path('welcome',views.bienvenida),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('createrecipe',views.create_recipe),
    #Apartado Mis Recetas
    path('myrecipes',views.myrecipes),

    #Apartado lista de recetas
    path('listaIngredientes', views.ingredient_list),

    #Detalles de recetas
    path('verRecetas/<int:pk>',
       RecipeDetail.as_view(),
         name='recipe_details'),

]
