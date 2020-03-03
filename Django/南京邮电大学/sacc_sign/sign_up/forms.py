from django import forms
from .models import Team_info

class TeamInfoForm(forms.ModelForm):
    class Meta:#储存管理模型的额外信息
        model = Team_info

        # 用来表示在前端使用form时显示哪些，就像本行表示，name，student_id，college显示而日期不显示
        fields = [
            'team_name','team_key'
        ]

        # 用来表示表单前的介绍如不加则默认为数据库中字段的名字如name，student_id等等，使用label则前面则显示你设着的
        labels = {
            'team_name':'队伍名称',
            'team_key': '队伍密钥（队友可根据密钥添加已创建队伍）',
        }

