from django.urls import path
from apps.authors.views import register_view,register_create
app_name = 'apps.authors'

urlpatterns = [
      path('register/',register_view, name='register'),
      path('register/create/',register_create, name='create'),
]