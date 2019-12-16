from django.shortcuts import render, reverse, redirect
from repository import models
from web.forms import ServerForm


# Create your views here.
def server(request):
    all_servers = models.Server.objects.all()
    return render(request, 'web/server.html', {'all_servers': all_servers})


def server_add(request):
    form_obj = ServerForm()
    if request.method == 'POST':
        form_obj = ServerForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('server'))

    return render(request, 'form.html', {'form_obj': form_obj})


def server_edit(request, pk):
    obj = models.Server.objects.filter(pk=pk).first()
    form_obj = ServerForm(instance=obj)
    if request.method == 'POST':
        form_obj = ServerForm(request.POST,instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('server'))

    return render(request, 'form.html', {'form_obj': form_obj})
