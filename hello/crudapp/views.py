from django.shortcuts import render
from django.shortcuts import redirect
from crudapp.models import Task

#from django.core.exceptions import ObjectDoesNotExist
# from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods


# Create your views here.


def create(request):
    if request.method == "POST":
        new_task = request.POST.get('task')

        if new_task:
            Task.objects.create(text=new_task)

        return redirect('crudapp:read')       #PRZEKIEROWANIE

    return render(
        request,
        'crudapp/create.html'
    )


def read(request):
    tasks = Task.objects.all()

    return render(
        request,
        'crudapp/read.html',
        context = {
            'tasks':tasks
        }
    )


def update(request, pk):
    # obsługa bledu 404 (dla importu z komentarzem)
    # try:
    #     task = Task.objects.get(pk=pk)
    # except ObjectDoesNotExist:
    #     raise Http404

    task = get_object_or_404(Task, pk=pk)   #obsługa 404 w 1 linijce

    if request.method == "POST":
        modified_task = request.POST.get('task')

        task.text = modified_task
        task.save()

        return  redirect('crudapp:read')

    # print(pk)
    return render(
        request,
        'crudapp/update.html',
        context={
            'task': task
        }
    )


@ require_http_methods(['POST'])    #nie pozwala na usuwanie z urla
def delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()

    return redirect('crudapp:read')

