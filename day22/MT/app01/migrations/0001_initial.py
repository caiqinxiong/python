# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-12-22 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=128, verbose_name='项目名称')),
                ('project_desc', models.CharField(max_length=256, verbose_name='项目描述')),
            ],
        ),
    ]
