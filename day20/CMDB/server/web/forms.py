from django import forms
from repository import models


class BSForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class ServerForm(BSForm):
    class Meta:
        model = models.Server
        fields = '__all__'
