# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-11-24 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20191124_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]