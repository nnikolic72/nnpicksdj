# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodusers', '0005_auto_20150211_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gooduser',
            name='last_processed_date',
            field=models.DateTimeField(null=True, verbose_name=b'GoodUser processed date', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gooduser',
            name='number_of_followers',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gooduser',
            name='number_of_followings',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gooduser',
            name='number_of_media',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
    ]
