from django.db import models

# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=128, verbose_name='项目名称')
    project_desc = models.CharField(max_length=256, verbose_name='项目描述')

    def __str__(self):
        return self.project_name
class Case(models.Model):
    """  接口用例表 """
    case_project = models.ForeignKey(to="Project", verbose_name='所属项目')
    case_name = models.CharField(max_length=128, verbose_name='用例名称')
    case_desc = models.CharField(max_length=512, verbose_name='用例描述')
    case_url = models.CharField(max_length=128, verbose_name='用例的URL')
    case_method = models.CharField(max_length=20, verbose_name='用例请求类型')
    case_params = models.CharField(max_length=256, verbose_name='用例请求参数')
    case_expect = models.CharField(max_length=256, verbose_name='期望值')
    case_execute_status = models.IntegerField(
        choices=((1, '已通过'), (0, '未通过')),
        default=0,
        verbose_name='用例执行状态'
    )
    def __str__(self):
        return self.case_name




