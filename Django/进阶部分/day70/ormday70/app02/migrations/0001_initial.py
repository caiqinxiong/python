# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-14 02:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Author2Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app02.Author')),
            ],
        ),
        migrations.CreateModel(
            name='AuthorDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobby', models.CharField(max_length=32)),
                ('addr', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('publish_date', models.DateField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app02.Publisher'),
        ),
        migrations.AddField(
            model_name='author2book',
            name='book_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app02.Book'),
        ),
        migrations.AddField(
            model_name='author',
            name='detail',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app02.AuthorDetail'),
        ),
    ]
