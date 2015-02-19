# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 18, 13, 7, 41, 359000), verbose_name=b'Photo creation date', auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='last_update_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 18, 13, 7, 41, 359000), verbose_name=b'Photo  creation date', auto_now=True),
            preserve_default=True,
        ),
    ]
