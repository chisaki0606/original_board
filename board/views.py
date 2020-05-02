from django.shortcuts import render, redirect, get_object_or_404
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

def update(request, pk):
  topic = get_object_or_404(Topic, pk=pk)
  form = TopicCreateForm(request.POST or None, instance=topic)
  if request.method == 'POST' and form.is_valid():
    form.save()
    return redirect('board:index')
  context = {
    'form':form
  }
  return render(request, 'board/form.html', context)

def delete(request, pk):
  topic = get_object_or_404(Topic, pk=pk)
  if request.method == 'POST':
    topic.delete()
    return redirect('board:index')
  context = {
    'topic':topic,
  }
  return render(request, 'board/confirm_delete.html', context)

def detail(request, pk):
  topic = get_object_or_404(Topic, pk=pk)
  context = {
    'topic':topic,
  }
  return render(request, 'board/detail.html', context)