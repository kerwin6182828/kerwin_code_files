# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-09 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='u_gender',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
