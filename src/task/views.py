from django.shortcuts import render
from django.http import HttpResponseRedirect
from task.models import TodoTask, Category
from task.forms import TaskCreateForm

def show_task(request):
    query = TodoTask.objects.all().order_by('created')

    # createform part
    form = TaskCreateForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    else:
        form = TaskCreateForm()

    dic = {
        'query': query,
        'form': form,
    }

    return render(request, 'task/index.html', dic)
