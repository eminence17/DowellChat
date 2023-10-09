from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('createroom', views.CreateRoom.as_view()),
    path('fetchroom/', views.get_room),

]