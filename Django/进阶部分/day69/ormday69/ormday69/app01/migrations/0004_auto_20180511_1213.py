# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-11 04:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='kucun',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='book',
            name='maichu',
            field=models.IntegerField(default=0),
        ),
    ]
