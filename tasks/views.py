from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Keyword, Task


@login_required(login_url='/accounts/login/')
def frontend(request):
    """Vue.js will take care of everything else."""
    keywords = Keyword.objects.all()
    tasks = Task.objects.all()

    data = {
        'keywords': keywords,
        'tasks': tasks,
    }

    return render(request, 'tasks/template.html', data)
