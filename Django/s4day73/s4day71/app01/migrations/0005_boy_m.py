# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-28 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20170628_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='boy',
            name='m',
            field=models.ManyToManyField(to='app01.Girl'),
        ),
    ]
