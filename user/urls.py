from django.urls import path
from .views import UserDetails, UserList
urlpatterns = [
    path('', UserList.as_view(), name="userlist"),
    path('<int:pk>/', UserDetails.as_view(), name="userdetail")
]
