# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-13 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0014_auto_20180913_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='u_portrait',
            field=models.CharField(default='/static/img/default.jpg/', max_length=500),
        ),
    ]
