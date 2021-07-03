from django.shortcuts import render

# Create your views here.


def register (request):
    #TASKS.append(request.POST.get('task'))
   # print(request.POST.get('task'))
  #  print(TASKS)
    return render(
        request,
        'formapp3/register.html',
    )


def tasks_list(request):

    # task = request.POST.get('task')
    # if task:
    #     TASKS.append(task)

    #ZAPIS DO PLIKU:

    with open('tasks.txt', 'a+') as f:
        task = request.POST.get('task')
        if task:
            f.write(task+"\n")

    with open('tasks.txt', 'r') as f:
        tasks = f.readlines()

    return render(
        request,
        'formapp3/tasks_list.html',
        context={
            "tasks": tasks
        }
    )