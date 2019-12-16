from django.shortcuts import render, reverse, redirect
from repository import models
from web.forms import ServerForm, BusinessUnitForm


def index(request):
    return render(request,'web/index.html')

# Create your views here.
def server(request):
    all_servers = models.Server.objects.all()
    return render(request, 'web/server.html', {'all_servers': all_servers})


def business_unit(request):
    all_business_units = models.BusinessUnit.objects.all()
    return render(request, 'web/business_unit.html', {'all_business_units': all_business_units})


def business_unit_change(request, pk=None):
    obj = models.BusinessUnit.objects.filter(pk=pk).first()
    form_obj = BusinessUnitForm(instance=obj)
    if request.method == 'POST':
        form_obj = BusinessUnitForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('business_unit')

    return render(request, 'form.html', {'form_obj': form_obj})


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
        form_obj = ServerForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('server'))

    return render(request, 'form.html', {'form_obj': form_obj})


def server_detail(request, pk):
    server_obj = models.Server.objects.filter(pk=pk).first()
    memory_list = server_obj.memory_list.all().order_by('slot')
    disk_list = server_obj.disk_list.all().order_by('slot')
    return render(request, 'web/server_detail.html', {
        'server_obj': server_obj,
        'memory_list': memory_list,
        'disk_list': disk_list,

    })


def server_record(request, pk):
    all_records = models.AssetRecord.objects.filter(server_id=pk).order_by('-create_at')
    return render(request, 'web/server_record.html', {'all_records': all_records})
