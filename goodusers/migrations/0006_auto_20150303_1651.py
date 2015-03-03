# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodusers', '0005_gooduser_user_attribute'),
    ]

    operations = [
        migrations.AddField(
            model_name='gooduser',
            name='last_processed_friends_date',
            field=models.DateTimeField(null=True, verbose_name=b'GoodUser processed date', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gooduser',
            name='to_be_processed_for_friends',
            field=models.BooleanField(default=True, help_text='Check if you want this Good User to be processed for friends in the next Batch Run'),
            preserve_default=True,
        ),
    ]
