# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-07 04:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_auto_20180707_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applynew',
            name='a3',
        ),
        migrations.AddField(
            model_name='applynew',
            name='A3',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='applynew',
            name='agent',
            field=models.CharField(max_length=30, null=True),
        ),
    ]