# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-08-10 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmsserver', '0003_auto_20170810_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='service_command',
            field=models.CharField(default=1, max_length=128, verbose_name='\u542f\u52a8\u547d\u4ee4'),
        ),
    ]
