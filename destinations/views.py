from django.shortcuts import render, redirect
from .models import Destination
from .forms import DestinationForm

def destination_list(request):
    context = {
        "destinations":Destination.objects.all()
    }
    return render(request, 'list.html', context)


def destination_detail(request, destination_id):
    context = {
        "destination": Destination.objects.get(id=destination_id)
    }
    return render(request, 'detail.html', context)

def destination_create(request):
    form = DestinationForm()
    if request.method == "POST":
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('destination-list')
    context = {
        "form":form,
    }
    return render(request, 'create.html', context)

def destination_update(request, destination_id):
    destination_obj = Destination.objects.get(id=destination_id)
    form = DestinationForm(instance=destination_obj)
    if request.method == "POST":
        form = DestinationForm(request.POST, instance=destination_obj)
        if form.is_valid():
            form.save()
            return redirect('destination-list')
    context = {
        "destination_obj": destination_obj,
        "form":form,
    }
    return render(request, 'update.html', context)

def destination_delete(request, destination_id):
    destination_obj = Destination.objects.get(id=destination_id)
    destination_obj.delete()
    return redirect('destination-list')
