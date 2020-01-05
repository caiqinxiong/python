from django.forms import ModelForm

class BootStrapModelForm(ModelForm):
    exclude_bootstrap = []

    def __init__(self,*args,**kwargs):
        # 执行父类的 __init__
        super().__init__(*args,**kwargs)

        # 自定义功能,为字段添加bootstrap样式
        for k,field in self.fields.items():
            if k in self.exclude_bootstrap:
                continue
            field.widget.attrs['class'] = 'form-control'
