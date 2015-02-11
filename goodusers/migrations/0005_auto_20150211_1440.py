# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodusers', '0004_auto_20150211_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gooduser',
            name='times_processed',
            field=models.IntegerField(default=0, verbose_name=b'Number of times processed'),
            preserve_default=True,
        ),
    ]
