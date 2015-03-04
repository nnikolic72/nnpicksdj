# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodusers', '0009_auto_20150304_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gooduser',
            name='to_be_processed_for_followings',
            field=models.BooleanField(default=True, help_text='Check if you want this Instagram user to be processed for Followings in the next Batch Run', verbose_name=b'TBP Followings'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gooduser',
            name='to_be_processed_for_friends',
            field=models.BooleanField(default=False, help_text='Check if you want this Instagram user to be processed for friends in the next Batch Run', verbose_name=b'TBP Friends'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gooduser',
            name='to_be_processed_for_photos',
            field=models.BooleanField(default=True, help_text='Check if you want this Instagram user to be processed for Photos in the next Batch Run', verbose_name=b'TBP Photos'),
            preserve_default=True,
        ),
    ]
