
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path('sent_msg/<str:pk>',views.sendMessages, name="sentmsg"),
    path('rece_msg/<str:pk>',views.recieve_chat, name="recemsg"),
     path('detail/<str:pk>',views.detail, name="detail"),
     path('notifications/',views.chat_notifications, name="chatnot"),
]