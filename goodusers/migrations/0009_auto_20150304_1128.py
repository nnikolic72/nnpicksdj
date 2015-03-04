# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodusers', '0008_auto_20150304_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gooduser',
            name='to_be_processed_for_basic_info',
            field=models.BooleanField(default=True, help_text='Check if you want this Instagram user to be processed in the next Batch Run', verbose_name=b'TBP Basic Info'),
            preserve_default=True,
        ),
    ]
