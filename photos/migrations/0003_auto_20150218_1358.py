# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20150218_1307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='comments',
            new_name='instagram_comments',
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='likes',
            new_name='instagram_likes',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='instagram_user_id',
        ),
        migrations.AddField(
            model_name='photo',
            name='instagram_photo_valid',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 18, 13, 58, 44, 515000), verbose_name=b'Photo creation date', auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='last_update_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 18, 13, 58, 44, 515000), verbose_name=b'Photo last update date', auto_now=True),
            preserve_default=True,
        ),
    ]
