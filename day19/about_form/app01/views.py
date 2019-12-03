from django.shortcuts import render, HttpResponse

from django import forms
from app01 import models

from django.core.exceptions import ValidationError


class PubForm(forms.Form):
    name = forms.CharField(label='姓名')

    def clean_name(self):
        # 通过校验规则 返回当前字段的值
        # 不通过校验规则 抛出异常 ValidationError
        pass

    def clean(self):
        # self.cleaned_data
        # 通过校验规则 返回所有字段的值
        # self.add_error()
        # 不通过校验规则 抛出异常 ValidationError
        pass


def pub_add(request):
    form_obj = PubForm()
    if request.method == 'POST':
        form_obj = PubForm(request.POST)
        if form_obj.is_valid():
            models.Publisher.objects.create(**form_obj.cleaned_data)

    return render(request, 'pub_add.html', {'form_obj': form_obj})


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = "__all__"  # ['name']
        # exclude = ['name']

        # labels = {'name':'书名'}

    def clean(self):
        self._validate_unique = True  # 在数据库校验唯一性
        return self.cleaned_data


def book_add(request):
    form_obj = BookForm()
    if request.method == 'POST':
        form_obj = BookForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()

    return render(request, 'form.html', {'form_obj': form_obj})


def index(request):
    return HttpResponse('index')
