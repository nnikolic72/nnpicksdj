# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='photo_rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, blank=True, help_text=b'Photo rating relative to users other photos', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 19, 10, 10, 35, 242000), verbose_name=b'Photo creation date', auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='last_update_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 19, 10, 10, 35, 242000), verbose_name=b'Photo last update date', auto_now=True),
            preserve_default=True,
        ),
    ]
