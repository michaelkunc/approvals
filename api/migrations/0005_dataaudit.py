# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-04 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20170604_0029'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataAudit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run_date', models.DateTimeField(auto_now_add=True)),
                ('run_type', models.CharField(max_length=30)),
            ],
        ),
    ]
