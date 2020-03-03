# Generated by Django 2.0.3 on 2018-03-21 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sign_up', '0009_actor_info_is_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=50)),
                ('member1', models.CharField(blank=True, default=None, max_length=50)),
                ('college1', models.CharField(blank=True, default=None, max_length=50)),
                ('tel1', models.CharField(blank=True, default=None, max_length=11)),
                ('student_id1', models.CharField(blank=True, default=None, max_length=9)),
                ('email1', models.EmailField(blank=True, default=None, max_length=254)),
                ('member2', models.CharField(blank=True, default=None, max_length=50)),
                ('college2', models.CharField(blank=True, default=None, max_length=50)),
                ('tel2', models.CharField(blank=True, default=None, max_length=11)),
                ('student_id2', models.CharField(blank=True, default=None, max_length=9)),
                ('email2', models.EmailField(blank=True, default=None, max_length=254)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='actor_info',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Actor_info',
        ),
    ]
