# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('tmsserver', '0010_auto_20170827_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='Content',
            field=DjangoUeditor.models.UEditorField(default=1, verbose_name='\u5185\u5bb9', blank=True),
        ),
    ]
