# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='photo_attributes',
            new_name='user_attribute',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='photo_categories',
            new_name='user_category',
        ),
        migrations.RemoveField(
            model_name='member',
            name='last_processed_date',
        ),
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=75, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='eyeem_handle',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='facebook_handle',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='full_name',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='iconosquare_user_profile_page_URL',
            field=models.URLField(default=b'', max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='instagram_profile_picture_URL',
            field=models.URLField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='instagram_user_bio',
            field=models.TextField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='instagram_user_full_name',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='instagram_user_id',
            field=models.CharField(max_length=100, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='instagram_user_name',
            field=models.CharField(default='', unique=True, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='instagram_user_name_valid',
            field=models.BooleanField(default=True, help_text='Check if Instagram user is valid/exists.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='instagram_user_profile_page_URL',
            field=models.URLField(default=b'', max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='instagram_user_website_URL',
            field=models.URLField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='is_user_active',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='last_processed_for_basic_info_date',
            field=models.DateTimeField(null=True, verbose_name=b'Instagram user processed date for basic info', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='last_processed_for_followings_date',
            field=models.DateTimeField(null=True, verbose_name=b'Instagram user processed for Followings date', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='last_processed_for_friends_date',
            field=models.DateTimeField(null=True, verbose_name=b'Instagram user processed for friends date', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='last_processed_for_photos_date',
            field=models.DateTimeField(null=True, verbose_name=b'Instagram user processed for Photos date', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='membership_expiry_date',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='number_of_followers',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='number_of_followings',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='number_of_media',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='paid_member',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='times_processed_for_basic_info',
            field=models.IntegerField(default=0, verbose_name=b'Number of times Instagram user was processed for basic info'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='times_processed_for_followings',
            field=models.IntegerField(default=0, verbose_name=b'Number of times Instagram user was processed for Followings'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='times_processed_for_friends',
            field=models.IntegerField(default=0, verbose_name=b'Number of times Instagram user was processed for friends'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='times_processed_for_photos',
            field=models.IntegerField(default=0, verbose_name=b'Number of times Instagram user was processed for Photos'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='to_be_processed_for_basic_info',
            field=models.BooleanField(default=True, help_text='Check if you want this Instagram user to be processed in the next Batch Run', verbose_name=b'TBP Basic Info'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='to_be_processed_for_followings',
            field=models.BooleanField(default=True, help_text='Check if you want this Instagram user to be processed for Followings in the next Batch Run', verbose_name=b'TBP Followings'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='to_be_processed_for_friends',
            field=models.BooleanField(default=False, help_text='Check if you want this Instagram user to be processed for friends in the next Batch Run', verbose_name=b'TBP Friends'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='to_be_processed_for_photos',
            field=models.BooleanField(default=True, help_text='Check if you want this Instagram user to be processed for Photos in the next Batch Run', verbose_name=b'TBP Photos'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='twitter_handle',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
