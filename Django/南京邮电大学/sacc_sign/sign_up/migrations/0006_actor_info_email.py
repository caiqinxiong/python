# Generated by Django 2.0.3 on 2018-03-16 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_up', '0005_auto_20180316_0510'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor_info',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
