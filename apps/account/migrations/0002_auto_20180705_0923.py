# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-07-05 01:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='userhead/defalut.png', upload_to='userhead/%Y/m'),
        ),
        migrations.AddField(
            model_name='user',
            name='work_position',
            field=models.CharField(default='这个人很懒,什么都没有留下', max_length=20),
        ),
    ]
