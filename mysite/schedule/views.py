from django.shortcuts import render, redirect
from .models import Schedule
from .forms import ScheduleForm

def index(request):
    schedules = Schedule.objects.all()
    return render(request, "schedule/index.html", {"schedules": schedules})

def add_schedule(request):
    if request.method == "POST":
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ScheduleForm()
    return render(request, "schedule/add.html", {"form": form})
