from django.urls import path,include
from django.urls import path
from apps.siga.views import HomeView,login_view

app_name = 'siga'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('', login_view, name='login'),
  ]