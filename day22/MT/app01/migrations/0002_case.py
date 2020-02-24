# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-12-22 07:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_name', models.CharField(max_length=128, verbose_name='用例名称')),
                ('case_desc', models.CharField(max_length=512, verbose_name='用例描述')),
                ('case_url', models.CharField(max_length=128, verbose_name='用例的URL')),
                ('case_method', models.CharField(max_length=20, verbose_name='用例请求类型')),
                ('case_params', models.CharField(max_length=256, verbose_name='用例请求参数')),
                ('case_expect', models.CharField(max_length=256, verbose_name='期望值')),
                ('case_execute_status', models.IntegerField(choices=[(1, '已通过'), (0, '未通过')], default=0, verbose_name='用例执行状态')),
                ('case_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Project', verbose_name='所属项目')),
            ],
        ),
    ]