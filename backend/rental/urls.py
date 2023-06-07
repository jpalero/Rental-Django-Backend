from django.urls import path
from .views import UserList, UserDetail

urlpatterns = [
    path('UserInfo/', UserList.as_view()),
    path('UserInfo/<int:pk>/', UserDetail.as_view()),
]