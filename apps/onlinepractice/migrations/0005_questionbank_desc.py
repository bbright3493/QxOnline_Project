# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-01-12 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinepractice', '0004_auto_20180112_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionbank',
            name='desc',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='\u9898\u5e93\u63cf\u8ff0'),
        ),
    ]
