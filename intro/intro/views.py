from django.shortcuts import HttpResponse
from django.shortcuts import render

#WIDOKI


# #tak nie robimy:
def hello(request):         #HTTP request
    return HttpResponse("<!DOCTYPE html><html><head><meta><title>Witaj!</title></head><body><h2>Hello, world</h2></body></html>")     #HTTP Response


def hello2(request):
    return render(
        request, "hello.html"
    )