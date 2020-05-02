from django.shortcuts import render, redirect
from .forms import TopicCreateForm
from .models import Topic

def index(request):
  context = {
    'list':Topic.objects.all(),
  }
  return render(request, 'board/list.html', context)

def add(request):
  form = TopicCreateForm(request.POST or None)
  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('board:index')
  context = {
    'form':form
  }
  return render(request, 'board/form.html', context)