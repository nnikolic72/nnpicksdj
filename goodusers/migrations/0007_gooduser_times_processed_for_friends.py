# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodusers', '0006_auto_20150303_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='gooduser',
            name='times_processed_for_friends',
            field=models.IntegerField(default=0, verbose_name=b'Number of times processed'),
            preserve_default=True,
        ),
    ]
