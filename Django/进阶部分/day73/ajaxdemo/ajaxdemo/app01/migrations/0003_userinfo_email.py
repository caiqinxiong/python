# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-17 03:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_userinfo_pwd'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
