# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-17 09:16
from __future__ import unicode_literals

import app02.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0007_auto_20191117_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.BooleanField(choices=[(True, '男'), (False, '女')], default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(blank=True, null=True, verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='user',
            name='bitrh',
            field=models.DateTimeField(auto_now=True, verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(db_column='username', max_length=32, unique=True, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=app02.models.MyCharField(max_length=11, verbose_name='手机号'),
        ),
    ]