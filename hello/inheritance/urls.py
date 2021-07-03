from django.urls import path

from inheritance import views

app_name = 'inheritance' #przestrzeń nazwy mapowań!

urlpatterns = [
    path('first', views.first, name='first'),
    path('second', views.second, name='second'),
]