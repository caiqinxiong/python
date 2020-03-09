from django.shortcuts import render
from django.views import View

from plug_ins.plug import pagination
from . import config


class IndexView(View):
    """
        首页展示
    """

    def get(self, request):
        massages = config.massages
        keys = ['ID', 'StuNum', 'Grade']
        contacts, part_page = pagination(request, massages, keys, 7)
        return render(request, 'index.html', {'contacts': contacts, 'part_page': part_page})
