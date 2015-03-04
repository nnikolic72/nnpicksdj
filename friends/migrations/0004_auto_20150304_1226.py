# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0003_auto_20150304_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='user_type',
            field=models.CharField(default=b'friend', max_length=50, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='friend',
            name='to_be_processed_for_basic_info',
            field=models.BooleanField(default=True, help_text='Check if you want this Instagram user to be processed in the next Batch Run', verbose_name=b'TBP Basic Info'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='friend',
            name='to_be_processed_for_followings',
            field=models.BooleanField(default=True, help_text='Check if you want this Instagram user to be processed for Followings in the next Batch Run', verbose_name=b'TBP Followings'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='friend',
            name='to_be_processed_for_friends',
            field=models.BooleanField(default=False, help_text='Check if you want this Instagram user to be processed for friends in the next Batch Run', verbose_name=b'TBP Friends'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='friend',
            name='to_be_processed_for_photos',
            field=models.BooleanField(default=True, help_text='Check if you want this Instagram user to be processed for Photos in the next Batch Run', verbose_name=b'TBP Photos'),
            preserve_default=True,
        ),
    ]
