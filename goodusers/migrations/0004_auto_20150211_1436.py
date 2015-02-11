# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodusers', '0003_auto_20150211_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='gooduser',
            name='last_processed_date',
            field=models.DateTimeField(null=True, verbose_name=b'GoodUser processed date'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gooduser',
            name='times_processed',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gooduser',
            name='to_be_processed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
