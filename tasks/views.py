from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework import viewsets

from .models import Keyword, Task
from .serializers import UserSerializer, KeywordSerializer, TaskSerializer

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


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
