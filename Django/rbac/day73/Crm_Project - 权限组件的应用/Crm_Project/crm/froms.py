from django import forms
from crm import models
from django.core.exceptions import ValidationError
import hashlib


# BootstropForm
class BSForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 自定义操作
        for field in self.fields.values():
            if not isinstance(field, forms.BooleanField):
                # field.widget.attrs['class'] = 'form-control'
                field.widget.attrs.update({'class': 'form-control'})


# 注册的form
class RegForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='密码', min_length=6)  # 重写默认字段
    re_password = forms.CharField(widget=forms.PasswordInput, label='确认密码', min_length=6)  # 新增字段

    class Meta:
        model = models.UserProfile  # 指定model
        fields = '__all__'  # ['username','password']  # 指定字段
        exclude = ['is_active']

        labels = {
            'username': '用户名'
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '用户名'}),
            # 'password': forms.PasswordInput(attrs={'class': 'form-control'})

        }
        error_messages = {

            'min_length': '不能少于6位'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 自定义操作
        for field in self.fields.values():
            # field.widget.attrs['class'] = 'form-control'
            field.widget.attrs.update({'class': 'form-control'})

    def clean(self):
        pwd = self.cleaned_data.get('password', '')
        re_pwd = self.cleaned_data.get('re_password', '')

        if pwd == re_pwd:
            # 密码加密
            md5 = hashlib.md5()
            md5.update(pwd.encode('utf-8'))
            pwd = md5.hexdigest()

            self.cleaned_data['password'] = pwd
            return self.cleaned_data
        # 两次密码不一致
        self.add_error('re_password', '两次密码不一致!!')
        raise ValidationError('两次密码不一致')


# 客户的form
class CustomerForm(BSForm):
    class Meta:
        model = models.Customer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].widget.attrs.pop('class')


# 跟进记录的form
class ConsultForm(BSForm):
    class Meta:
        model = models.ConsultRecord
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # print(list(self.fields['customer'].choices))  # 可选的参数
        # print(self.instance.consultant)  # 当前的销售

        customer_choices = [('', '---------')]

        # 限制可选的客户为 当前销售的客户
        self.fields['customer'].choices = customer_choices + [(i.pk, str(i)) for i in
                                                              self.instance.consultant.customers.all()]
        # 限制可销售为 当前销售
        self.fields['consultant'].choices = [(self.instance.consultant_id, self.instance.consultant), ]


# 报名记录的form
class EnrollmentForm(BSForm):
    class Meta:
        model = models.Enrollment
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 限制客户为 customer_id 的客户
        self.fields['customer'].choices = [(self.instance.customer_id, self.instance.customer)]
        # 客户
        print(self.instance.customer.class_list.all())
        # 限制报名班级为已报名的班级
        self.fields['enrolment_class'].choices = [(i.pk, str(i)) for i in self.instance.customer.class_list.all()]


# 班级的form
class ClassListForm(BSForm):
    class Meta:
        model = models.ClassList
        fields = "__all__"


# 课程记录的form
class CourseRecordForm(BSForm):
    class Meta:
        model = models.CourseRecord
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CourseRecordForm, self).__init__(*args, **kwargs)
        # 限制班级
        self.fields['re_class'].choices = [(self.instance.re_class_id, self.instance.re_class)]
        # 限制班主任
        self.fields['teacher'].choices = [(self.instance.teacher_id, self.instance.teacher)]


from django.core.exceptions import ValidationError


# 学习记录的form
class StudyRecordForm(BSForm):
    class Meta:
        model = models.StudyRecord
        fields = "__all__"

    def clean_note(self):
        note = self.cleaned_data.get('note', '')
        if not note:
            note = ''
        if '666' in note:
            raise ValidationError('不能太6')

        return note
