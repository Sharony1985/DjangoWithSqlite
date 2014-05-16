from django.shortcuts import render

# Create your views here.
from polls.models import Task

def index(request):
    task_list = Task.objects.all()
    context = {'task_list': task_list}
    return render(request, 'polls/index.html', context)