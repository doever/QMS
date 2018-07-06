# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-07-05 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20180705_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='jobs',
            field=models.CharField(default='员工', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='userhead/defalut.png', upload_to='userhead/%Y/%m'),
        ),
    ]
