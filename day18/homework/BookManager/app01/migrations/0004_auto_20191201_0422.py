# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-12-01 04:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20191201_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Publisher', verbose_name='出版社'),
        ),
    ]
