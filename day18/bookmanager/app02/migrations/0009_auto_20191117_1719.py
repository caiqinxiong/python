# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-17 09:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0008_auto_20191117_1716'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '个人信息', 'verbose_name_plural': '所有用户信息'},
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
