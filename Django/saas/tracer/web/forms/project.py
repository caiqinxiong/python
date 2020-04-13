from django import forms
from django.core.exceptions import ValidationError

from web.forms.bootstrap import BootstrapForm
from web.forms.widgets import ColorRadioSelect
from web import models

class ProjectModelForm(BootstrapForm, forms.ModelForm):
    bootstrap_class_exclude = ['color']
    class Meta:
        model = models.Project
        fields = ['name','color','desc']
        widgets = {
            'desc':forms.Textarea,
            'color': ColorRadioSelect(attrs={'class': 'color-radio'}),
        }

    def __init__(self,request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def clean_name(self):
        name = self.cleaned_data['name']
        exists = models.Project.objects.filter(name=name,creator=self.request.tracer.user).exists()
        if exists:
            raise ValidationError('项目名已存在')
        count = models.Project.objects.filter(creator=self.request.tracer.user).count()
        if count >= self.request.tracer.price_policy.project_num:
            raise ValidationError('项目个数超限,请升级套餐')
        return name














