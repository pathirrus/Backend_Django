from django.shortcuts import render

# Create your views here.

TASKS=[]
def register (request):



    #TASKS.append(request.POST.get('task'))
   # print(request.POST.get('task'))
  #  print(TASKS)
    return render(
        request,
        'formapp2/register.html',
    )


def tasks_list(request):

    task = request.POST.get('task')
    if task:
        TASKS.append(task)

    return render(
        request,
        'formapp2/tasks_list.html',
        context={
            "tasks": TASKS
        }
    )