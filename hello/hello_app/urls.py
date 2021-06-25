from django.urls import path

from hello_app import views         # pycharm podkreślna bo nie ma dodatku dla Django

urlpatterns = [

    path('hello/', views.hello),
    path('time/', views.show_time),
    path('welcome/', views.welcome),
]