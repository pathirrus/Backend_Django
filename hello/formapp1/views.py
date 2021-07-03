from django.shortcuts import render

# Create your views here.

TASKS=[]
def register (request):
    task = request.GET.get('task')
    if task:
        TASKS.append(task)
    #TASKS.append(request.GET.get('task'))
   # print(request.GET.get('task'))
    print(TASKS)
    return render(
        request,
        'formapp1/register.html',
        context={
            "tasks": TASKS
        }
    )