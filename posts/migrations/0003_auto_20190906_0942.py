# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-06 09:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20190906_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
