# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20150219_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='instagram_photo_processed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 19, 13, 57, 25, 636000), verbose_name=b'Photo creation date', auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='last_update_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 19, 13, 57, 25, 636000), verbose_name=b'Photo last update date', auto_now=True),
            preserve_default=True,
        ),
    ]
