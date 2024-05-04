from django.shortcuts import render, redirect
from tracker.models import Task
from django.contrib import messages
from tracker.forms import AddTaskForm

def tracker(request):
    form = AddTaskForm()
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddTaskForm(request.POST)
            if form.is_valid():
                form.instance.user = request.user
                form.save()
                messages.success(request, 'Task has been added')
                return redirect('tracker')
        # Show added tasks
        current_user = request.user
        tasks = Task.objects.filter(user=current_user)
        return render(request, 'tracker/tracker.html', {'tasks': tasks, 'form':form})
    else:
        messages.success(request, 'You must be logged in to add tasks')
        return redirect('index')
