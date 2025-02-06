from django.urls import path
from apps.authors.views import (register_view,register_create,login_view,login_create,
                                logout_view,dashboard,dashboard_recipe_edit,dashboard_recipe_new,
                                dashboard_recipe_delete)
app_name = 'apps.authors'

urlpatterns = [
      path('register/',register_view, name='register'),
      path('register/create/',register_create, name='register_create'),
      
      path('login/',login_view, name='login'),
      path('login/create',login_create, name='login_create'),
      
      path('logout/',logout_view, name='logout'),
      
      path('dashboard/',dashboard, name='dashboard'),
      path('dashboard/receita/nova/',dashboard_recipe_new,name='dashboard_recipe_new'),
      path('dashboard/receita/<int:id>/edit/',dashboard_recipe_edit,name='dashboard_recipe_edit'),
      path('dashboard/receita/delete/',dashboard_recipe_delete, name='dashboard_recipe_delete'),
      
]