# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-17 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0006_auto_20191117_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(db_column='username', max_length=32, unique=True),
        ),
    ]
