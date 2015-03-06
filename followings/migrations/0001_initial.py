# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodusers', '0011_gooduser_user_type'),
        ('categories', '0005_categoryraw'),
        ('attributes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Following',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
                ('twitter_handle', models.CharField(max_length=100, null=True, blank=True)),
                ('facebook_handle', models.CharField(max_length=100, null=True, blank=True)),
                ('eyeem_handle', models.CharField(max_length=100, null=True, blank=True)),
                ('instagram_user_name', models.CharField(unique=True, max_length=100)),
                ('instagram_user_name_valid', models.BooleanField(default=True, help_text='Check if Instagram user is valid/exists.')),
                ('instagram_user_id', models.CharField(max_length=100, unique=True, null=True, blank=True)),
                ('instagram_user_profile_page_URL', models.URLField(default=b'', max_length=255, null=True, blank=True)),
                ('iconosquare_user_profile_page_URL', models.URLField(default=b'', max_length=255, null=True, blank=True)),
                ('instagram_profile_picture_URL', models.URLField(max_length=255, null=True, blank=True)),
                ('instagram_user_bio', models.TextField(max_length=500, null=True, blank=True)),
                ('instagram_user_website_URL', models.URLField(max_length=255, null=True, blank=True)),
                ('full_name', models.CharField(max_length=100, null=True, blank=True)),
                ('instagram_user_full_name', models.CharField(max_length=100, null=True, blank=True)),
                ('is_user_active', models.BooleanField(default=False)),
                ('number_of_followers', models.IntegerField(default=0, null=True, blank=True)),
                ('number_of_followings', models.IntegerField(default=0, null=True, blank=True)),
                ('number_of_media', models.IntegerField(default=0, null=True, blank=True)),
                ('times_processed_for_basic_info', models.IntegerField(default=0, verbose_name=b'Number of times Instagram user was processed for basic info')),
                ('last_processed_for_basic_info_date', models.DateTimeField(null=True, verbose_name=b'Instagram user processed date for basic info', blank=True)),
                ('to_be_processed_for_basic_info', models.BooleanField(default=True, help_text='Check if you want this Instagram user to be processed in the next Batch Run', verbose_name=b'TBP Basic Info')),
                ('last_processed_for_friends_date', models.DateTimeField(null=True, verbose_name=b'Instagram user processed for friends date', blank=True)),
                ('times_processed_for_friends', models.IntegerField(default=0, verbose_name=b'Number of times Instagram user was processed for friends')),
                ('to_be_processed_for_friends', models.BooleanField(default=False, help_text='Check if you want this Instagram user to be processed for friends in the next Batch Run', verbose_name=b'TBP Friends')),
                ('last_processed_for_followings_date', models.DateTimeField(null=True, verbose_name=b'Instagram user processed for Followings date', blank=True)),
                ('times_processed_for_followings', models.IntegerField(default=0, verbose_name=b'Number of times Instagram user was processed for Followings')),
                ('to_be_processed_for_followings', models.BooleanField(default=True, help_text='Check if you want this Instagram user to be processed for Followings in the next Batch Run', verbose_name=b'TBP Followings')),
                ('last_processed_for_photos_date', models.DateTimeField(null=True, verbose_name=b'Instagram user processed for Photos date', blank=True)),
                ('times_processed_for_photos', models.IntegerField(default=0, verbose_name=b'Number of times Instagram user was processed for Photos')),
                ('to_be_processed_for_photos', models.BooleanField(default=True, help_text='Check if you want this Instagram user to be processed for Photos in the next Batch Run', verbose_name=b'TBP Photos')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name=b'GoodUser creation date')),
                ('last_update_date', models.DateTimeField(auto_now=True, verbose_name=b'GoodUser creation date')),
                ('user_type', models.CharField(default=b'following', max_length=50, editable=False)),
                ('gooduser', models.ManyToManyField(to='goodusers.GoodUser', null=True, blank=True)),
                ('user_attribute', models.ManyToManyField(to='attributes.Attribute', null=True, blank=True)),
                ('user_category', models.ManyToManyField(to='categories.Category', null=True, blank=True)),
            ],
            options={
                'ordering': ('instagram_user_name',),
                'abstract': False,
                'get_latest_by': 'creation_date',
                'verbose_name': 'Following',
                'verbose_name_plural': 'Followings',
            },
            bases=(models.Model,),
        ),
    ]
