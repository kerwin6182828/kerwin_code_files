# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-11 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_auto_20180910_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='t_text',
            field=models.CharField(default=0, max_length=30),
        ),
    ]
