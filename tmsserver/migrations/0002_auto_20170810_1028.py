# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-08-10 02:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmsserver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service_address',
            field=models.CharField(default=1, max_length=128),
        ),
    ]
