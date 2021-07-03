from django.shortcuts import render

# Create your views here.


def register(request):
    return render(
        request,
        'formapp4/register.html'
    )

def tasks_list(request):
    return render(
        request,
        'formapp4/tasks_list.html',
        context={
            "tasks": tasks
        }
    )