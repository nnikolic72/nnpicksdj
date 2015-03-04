# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodusers', '0007_gooduser_times_processed_for_friends'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gooduser',
            options={'ordering': ('instagram_user_name',), 'get_latest_by': 'creation_date', 'verbose_name': 'Good User', 'verbose_name_plural': 'Good Users'},
        ),
        migrations.RemoveField(
            model_name='gooduser',
            name='last_processed_date',
        ),
        migrations.RemoveField(
            model_name='gooduser',
            name='last_processed_friends_date',
        ),
        migrations.RemoveField(
            model_name='gooduser',
            name='times_processed',
        ),
        migrations.RemoveField(
            model_name='gooduser',
            name='to_be_processed',
        ),
        migrations.RemoveField(
            model_name='gooduser',
            name='user_name',
        ),
        migrations.AddField(
            model_name='gooduser',
            name='last_processed_for_basic_info_date',
            field=models.DateTimeField(null=True, verbose_name=b'Instagram user processed date for basic info', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gooduser',
            name='last_processed_for_followings_date',
            field=models.DateTimeField(null=True, verbose_name=b'Instagram user processed for Followings date', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gooduser',
            name='last_processed_for_friends_date',
            field=models.DateTimeField(null=True, verbose_name=b'Instagram user processed for friends date', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gooduser',
            name='last_processed_for_photos_date',
            field=models.DateTimeField(null=True, verbose_name=b'Instagram user processed for Photos date', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gooduser',
            name='times_processed_for_basic_info',
            field=models.IntegerField(default=0, verbose_name=b'Number of times Instagram user was processed for basic info'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gooduser',
            name='times_processed_for_followings',
            field=models.IntegerField(default=0, verbose_name=b'Number of times Instagram user was processed for Followings'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gooduser',
            name='times_processed_for_photos',
            field=models.IntegerField(default=0, verbose_name=b'Number of times Instagram user was processed for Photos'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gooduser',
            name='to_be_processed_for_basic_info',
            field=models.BooleanField(default=True, help_text='Check if you want this Instagram user to be processed in the next Batch Run'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gooduser',
            name='to_be_processed_for_followings',
            field=models.BooleanField(default=True, help_text='Check if you want this Instagram user to be processed for Followings in the next Batch Run'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gooduser',
            name='to_be_processed_for_photos',
            field=models.BooleanField(default=True, help_text='Check if you want this Instagram user to be processed for Photos in the next Batch Run'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gooduser',
            name='times_processed_for_friends',
            field=models.IntegerField(default=0, verbose_name=b'Number of times Instagram user was processed for friends'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gooduser',
            name='to_be_processed_for_friends',
            field=models.BooleanField(default=False, help_text='Check if you want this Instagram user to be processed for friends in the next Batch Run'),
            preserve_default=True,
        ),
    ]
