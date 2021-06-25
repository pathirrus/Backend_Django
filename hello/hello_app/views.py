from django.shortcuts import render
from django.shortcuts import HttpResponse

import datetime
# Create your views here.

def hello(request):
    return render(
        request,
        'hello.html'            # dumyślnie szuka folderu templates
    )

def show_time(request):
    actual_time = datetime.datetime.now()
    return HttpResponse(f"Aktualny czas: {actual_time}")


def welcome(request):
    return render(
        request,
        'welcome.html'  # dumyślnie szuka folderu templates
    )