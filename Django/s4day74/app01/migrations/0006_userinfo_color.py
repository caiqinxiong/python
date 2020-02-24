# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-29 01:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_userinfo_ctime'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='color',
            field=models.IntegerField(choices=[(1, '黑色'), (2, '白色'), (3, '蓝色')], default=1),
            preserve_default=False,
        ),
    ]