# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(unique=True, max_length=100)),
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
                ('last_processed_date', models.DateTimeField(null=True, verbose_name=b'GoodUser processed date', blank=True)),
                ('times_processed', models.IntegerField(default=0, verbose_name=b'Number of times processed')),
                ('to_be_processed', models.BooleanField(default=True, help_text='Check if you want this Good User to be processed in the next Batch Run')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name=b'GoodUser creation date')),
                ('last_update_date', models.DateTimeField(auto_now=True, verbose_name=b'GoodUser creation date')),
            ],
            options={
                'ordering': ('user_name',),
                'get_latest_by': 'creation_date',
                'verbose_name': 'Good User',
                'verbose_name_plural': 'Good Users',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GoodUsersCategories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('good_user_id', models.IntegerField()),
                ('category_id', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
