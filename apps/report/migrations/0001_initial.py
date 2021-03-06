# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-06-28 06:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Applynew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billno', models.CharField(db_index=True, max_length=50, unique=True)),
                ('machinesid', models.CharField(db_index=True, max_length=50, null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('province', models.CharField(max_length=20, null=True)),
                ('city', models.CharField(max_length=20, null=True)),
                ('area', models.CharField(max_length=20, null=True)),
                ('billstate', models.IntegerField(db_index=True, null=True)),
                ('billsort', models.CharField(max_length=20, null=True)),
                ('isspecial', models.CharField(max_length=10, null=True)),
                ('agent', models.IntegerField(null=True)),
                ('areacode', models.CharField(db_index=True, max_length=30, null=True)),
                ('createdate', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('installdate', models.DateTimeField(db_index=True, null=True)),
                ('a3', models.CharField(max_length=10, null=True)),
                ('A7', models.CharField(max_length=10, null=True)),
                ('installer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '开户单',
                'verbose_name_plural': '开户单',
            },
        ),
    ]
