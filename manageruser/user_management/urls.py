from django.urls import path
from .views import (CreateUser,
                    user_list,
                    DeleteUser,
                    UpdateUser)

urlpatterns = [
    path('create/',CreateUser.as_view(),name='criar'),
    path('delete/<int:pk>/',DeleteUser.as_view(),name='delete_user'),
    path('update/<int:pk>/', UpdateUser.as_view(),name='update_user'),
    path('user_list/',user_list,name='user_list'),
]
