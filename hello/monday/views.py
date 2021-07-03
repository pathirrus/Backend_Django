from django.shortcuts import render
from datetime import datetime

# Create your views here.

def monday(request):
    is_it_monday= False
    now = datetime.now()

    if (now.weekday()==0):
        is_it_monday = True

    return render(
    request,
    'monday/monday.html',
    context = {
        "is_it_monday": is_it_monday
    }
    )