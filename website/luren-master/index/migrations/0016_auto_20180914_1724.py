# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-14 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0015_auto_20180913_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='a_collect',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='a_like_num',
            field=models.IntegerField(default=0),
        ),
    ]
