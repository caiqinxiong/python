# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-22 04:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='username',
            new_name='user',
        ),
    ]
