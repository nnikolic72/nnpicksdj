# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0005_categoryraw'),
        ('attributes', '0001_initial'),
        ('friends', '0002_friend_iconosquare_user_profile_page_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='last_processed_date',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='times_processed',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='to_be_processed',
        ),
        migrations.AddField(
            model_name='friend',
            name='email',
            field=models.EmailField(max_length=75, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='friend',
            name='eyeem_handle',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='friend',
            name='facebook_handle',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='friend',
            name='full_name',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='friend',
            name='last_processed_for_basic_info_date',
            field=models.DateTimeField(null=True, verbose_name=b'Instagram user processed date for basic info', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='friend',
            name='last_processed_for_followings_date',
            field=models.DateTimeField(null=True, verbose_name=b'Instagram user processed for Followings date', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='friend',
            name='last_processed_for_friends_date',
            field=models.DateTimeField(null=True, verbose_name=b'Instagram user processed for friends date', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='friend',
            name='last_processed_for_photos_date',
            field=models.DateTimeField(null=True, verbose_name=b'Instagram user processed for Photos date', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='friend',
            name='times_processed_for_basic_info',
            field=models.IntegerField(default=0, verbose_name=b'Number of times Instagram user was processed for basic info'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='friend',
            name='times_processed_for_followings',
            field=models.IntegerField(default=0, verbose_name=b'Number of times Instagram user was processed for Followings'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='friend',
            name='times_processed_for_friends',
            field=models.IntegerField(default=0, verbose_name=b'Number of times Instagram user was processed for friends'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='friend',
            name='times_processed_for_photos',
            field=models.IntegerField(default=0, verbose_name=b'Number of times Instagram user was processed for Photos'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='friend',
            name='to_be_processed_for_basic_info',
            field=models.BooleanField(default=True, help_text='Check if you want this Instagram user to be processed in the next Batch Run'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='friend',
            name='to_be_processed_for_followings',
            field=models.BooleanField(default=True, help_text='Check if you want this Instagram user to be processed for Followings in the next Batch Run'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='friend',
            name='to_be_processed_for_friends',
            field=models.BooleanField(default=False, help_text='Check if you want this Instagram user to be processed for friends in the next Batch Run'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='friend',
            name='to_be_processed_for_photos',
            field=models.BooleanField(default=True, help_text='Check if you want this Instagram user to be processed for Photos in the next Batch Run'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='friend',
            name='twitter_handle',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='friend',
            name='user_attribute',
            field=models.ManyToManyField(to='attributes.Attribute', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='friend',
            name='user_category',
            field=models.ManyToManyField(to='categories.Category', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='friend',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'GoodUser creation date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='friend',
            name='last_update_date',
            field=models.DateTimeField(auto_now=True, verbose_name=b'GoodUser creation date'),
            preserve_default=True,
        ),
    ]
